;WITH StudentHome AS (
  SELECT
    StudentID, 
    ISNULL(Latitude, 0) AS StudentLat, 
    ISNULL(Longitude, 0) AS StudentLong,
    GEOGRAPHY::STGeomFromText('POINT(' + CAST(ISNULL(Longitude, 0) AS VARCHAR(20)) + ' ' + CAST(ISNULL(Latitude, 0) AS VARCHAR(20)) + ')', 4326) AS StudentGeog
  FROM 
    [SEO_REPORTING].[dbo].[NPSStudentAddress_060324]
),
SchoolLocations AS (
  SELECT 
    SchoolDBN, 
    ISNULL(Latitude, 0) AS SchoolLat, 
    ISNULL(Longitude, 0) AS SchoolLong,
    GEOGRAPHY::STGeomFromText('POINT(' + CAST(ISNULL(Longitude, 0) AS VARCHAR(20)) + ' ' + CAST(ISNULL(Latitude, 0) AS VARCHAR(20)) + ')', 4326) AS SchoolGeog
  FROM 
    [SEO_MART].[dbo].[RPT_Locations]
  WHERE SchoolType = 'CSD' and ActiveFlag = 'Y'
),
DistanceCalculation AS (
  SELECT 
    sh.StudentID, 
    sl.SchoolDBN, 
    sh.StudentGeog.STDistance(sl.SchoolGeog) / 1609.344 AS Distance -- Distance in miles
  FROM 
    StudentHome sh
  CROSS JOIN 
    SchoolLocations sl
  WHERE
    sh.StudentGeog IS NOT NULL AND sl.SchoolGeog IS NOT NULL
),
RankedDistances AS (
  SELECT 
    StudentID, 
    SchoolDBN, 
    Distance, 
    ROW_NUMBER() OVER (PARTITION BY StudentID ORDER BY Distance, SchoolDBN) AS Rank -- Choose the lowest SchoolDBN if multiple schools have the same distance
  FROM 
    DistanceCalculation
),
FilteredRanks AS (
  SELECT 
    StudentID, 
    SchoolDBN
  FROM 
    RankedDistances
  WHERE 
    Rank = 1
),
ClosedStudentCount AS (
  SELECT 
    SchoolDBN, 
    COUNT(StudentID) AS [Nearby NPS Students]
  FROM 
    FilteredRanks
  GROUP BY 
    SchoolDBN
)
SELECT 
  SchoolDBN, 
  [Nearby NPS Students], 
  RANK() OVER (ORDER BY [Nearby NPS Students] DESC) AS SchoolRank
FROM 
  ClosedStudentCount
ORDER BY 
  SchoolRank;
