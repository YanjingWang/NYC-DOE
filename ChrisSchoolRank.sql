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
    ROW_NUMBER() OVER (PARTITION BY StudentID ORDER BY Distance) AS Rank
  FROM 
    DistanceCalculation
),
ClosedStudentCount AS (
  SELECT 
    SchoolDBN, 
    COUNT(StudentID) AS ClosedStudents
  FROM 
    RankedDistances
  WHERE 
    Rank = 1
  GROUP BY 
    SchoolDBN
)
SELECT 
  SchoolDBN, 
  ClosedStudents, 
  RANK() OVER (ORDER BY ClosedStudents DESC) AS SchoolRank
FROM 
  ClosedStudentCount
ORDER BY 
  SchoolRank;
