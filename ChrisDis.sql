WITH StudentHome AS (
  SELECT
    StudentID, 
    HouseNumberStreet,
    Boroughcode,
    Zipcode,
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
  WHERE 
    SchoolType = 'CSD' AND ActiveFlag = 'Y'
),
DistanceCalculation AS (
  SELECT 
    sh.StudentID, 
    sh.HouseNumberStreet,
    sh.Boroughcode,
    sh.Zipcode,
    sl.SchoolDBN, 
	sh.StudentLat,
	sh.StudentLong,
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
  StudentID, 
  HouseNumberStreet,
  Boroughcode,
  Zipcode,
  StudentLat,
  StudentLong,
  SchoolDBN, 
  Distance,
  COUNT(StudentID) AS [ClosedStudents]--OVER (PARTITION BY SchoolDBN) 
  
FROM 
  RankedDistances
WHERE 
  Rank = 1
--ORDER BY 
--  StudentID, 
--  HouseNumberStreet,
--  Boroughcode,
--  Zipcode,
--  SchoolDBN, 
--  StudentLat,
--  StudentLong,
--  Distance,
--  [ClosedStudents] DESC;
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
