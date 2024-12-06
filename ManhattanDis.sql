;WITH StudentHome AS (
  SELECT
    DISTINCT StudentID, 
    HouseNumberStreet,
    Boroughcode,
    Zipcode,
    ISNULL(Latitude, 0) AS StudentLat, 
    ISNULL(Longitude, 0) AS StudentLong
  FROM 
    [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] --NPS Students table
),
SchoolLocations AS (
  SELECT 
    SchoolDBN, 
    ISNULL(Latitude, 0) AS SchoolLat, 
    ISNULL(Longitude, 0) AS SchoolLong
  FROM 
    [SEO_MART].[dbo].[RPT_Locations]
	WHERE SchoolType = 'CSD' and ActiveFlag = 'Y'-- Replace with school table name with CSD conditions
),
DistanceCalculation AS (
  SELECT 
    DISTINCT sh.StudentID, 
    sh.HouseNumberStreet,
    sh.Boroughcode,
    sh.Zipcode,
    sl.SchoolDBN, 
    sh.StudentLat,
    sh.StudentLong,
    --ABS(sh.StudentLat - sl.SchoolLat) + ABS(sh.StudentLong - sl.SchoolLong) AS Distance -- Manhattan distance  75K231	1616
	6371 * ACOS(COS(RADIANS(sh.StudentLat)) 
            * COS(RADIANS(sl.SchoolLat)) 
            * COS(RADIANS(sl.SchoolLong) - RADIANS(sh.StudentLong)) 
            + SIN(RADIANS(sh.StudentLat)) 
            * SIN(RADIANS(sl.SchoolLat))) AS Distance -- Haversine formula 75K231 1698
    --SQRT(
    --  POWER(ISNULL(sh.StudentLat, 0) - ISNULL(sl.SchoolLat, 0), 2) + 
    --  POWER(ISNULL(sh.StudentLong, 0) - ISNULL(sl.SchoolLong, 0), 2)
    --) AS Distance -- Euclidean distance 75K231	1650
  FROM 
    StudentHome sh
  CROSS JOIN 
    SchoolLocations sl
),
RankedDistances AS (
  SELECT 
    DISTINCT StudentID, 
    HouseNumberStreet,
    Boroughcode,
    Zipcode,
    SchoolDBN, 
    Distance, 
    StudentLat,
    StudentLong,
    ROW_NUMBER() OVER (PARTITION BY StudentID ORDER BY Distance) AS Rank
  FROM 
    DistanceCalculation
)
SELECT 
  DISTINCT StudentID, 
  HouseNumberStreet,
  Boroughcode,
  Zipcode,
  StudentLat,
  StudentLong,
  SchoolDBN, 
  Distance,
  COUNT(StudentID) AS [ClosedStudents]

FROM 
  RankedDistances
WHERE 
  Rank = 1
GROUP BY 
  StudentID, 
  HouseNumberStreet,
  Boroughcode,
  Zipcode,
  StudentLat,
  StudentLong,
  SchoolDBN,
  Distance
ORDER BY 
  StudentID, 
  HouseNumberStreet,
  Boroughcode,
  Zipcode,
  StudentLat,
  StudentLong,
  SchoolDBN,
  Distance,
  [ClosedStudents] DESC;
