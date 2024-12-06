-- CREATE INDEX idx_NPSStudentAddress_LatLong ON [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] (StudentID, Latitude, Longitude);
-- CREATE INDEX idx_RPT_Locations_LatLong ON [SEO_MART].[dbo].[RPT_Locations] (SchoolDBN, Latitude, Longitude);
--CREATE INDEX IX_NPSStudentAddress060324StudentID 
--ON [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] (StudentID);

--CREATE INDEX IX_NPSStudentAddress060324Latitude 
--ON [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] (Latitude);

--CREATE INDEX IX_NPSStudentAddress060324Longitude 
--ON [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] (Longitude);

--CREATE INDEX IX_RPTLocationSchoolDBN 
--ON [SEO_MART].[dbo].[RPT_Locations] (SchoolDBN);

--CREATE INDEX IX_RPTLocationLatitude 
--ON [SEO_MART].[dbo].[RPT_Locations] (Latitude);

--CREATE INDEX IX_RPTLocationLongitude 
--ON [SEO_MART].[dbo].[RPT_Locations] (Longitude);

;WITH StudentHome AS (
  SELECT
    StudentID, 
    ISNULL(Latitude, 0) AS StudentLat, 
    ISNULL(Longitude, 0) AS StudentLong
  FROM 
    [SEO_REPORTING].[dbo].[NPSStudentAddress_060324] --NPS Students table
  GROUP BY 
    StudentID, 
    ISNULL(Latitude, 0), 
    ISNULL(Longitude, 0)
),
SchoolLocations AS (
  SELECT 
    SchoolDBN, 
    ISNULL(Latitude, 0) AS SchoolLat, 
    ISNULL(Longitude, 0) AS SchoolLong
  FROM 
    [SEO_MART].[dbo].[RPT_Locations] -- Replace with school table name
  GROUP BY 
    SchoolDBN, 
    ISNULL(Latitude, 0), 
    ISNULL(Longitude, 0)
),
DistanceCalculation AS (
  SELECT 
    sh.StudentID, 
    sl.SchoolDBN, 
    ABS(sh.StudentLat - sl.SchoolLat) + ABS(sh.StudentLong - sl.SchoolLong) AS Distance -- Manhattan distance
  FROM 
    StudentHome sh
  CROSS JOIN 
    SchoolLocations sl
),
RankedDistances AS (
  SELECT 
    StudentID, 
    SchoolDBN, 
    Distance, 
    ROW_NUMBER() OVER (PARTITION BY StudentID ORDER BY Distance) AS Rank
  FROM 
    DistanceCalculation
)
SELECT 
  SchoolDBN, 
  COUNT(StudentID) AS [ClosedStudents]
FROM 
  RankedDistances
WHERE 
  Rank = 1
GROUP BY 
  SchoolDBN;
