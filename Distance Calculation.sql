WITH StudentHome AS (
    SELECT 
        DISTINCT StudentID, 
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
        [SEO_MART].[dbo].[RPT_Locations] -- Replace with school table name
),
DistanceCalculation AS (
    SELECT 
        DISTINCT sh.StudentID,
        sl.SchoolDBN,
        ABS(ISNULL(sh.StudentLat, 0) - ISNULL(sl.SchoolLat, 0)) + ABS(ISNULL(sh.StudentLong, 0) - ISNULL(sl.SchoolLong, 0)) AS Distance -- Manhattan distance
    FROM 
        StudentHome sh
    CROSS JOIN 
        SchoolLocations sl
),
RankedDistances AS (
    SELECT 
        DISTINCT StudentID,
        SchoolDBN,
        Distance,
        ROW_NUMBER() OVER (PARTITION BY StudentID ORDER BY Distance) AS Rank
    FROM 
        DistanceCalculation
)
SELECT 
    StudentID,
    SchoolDBN,
    Distance
FROM 
    RankedDistances
WHERE 
    Rank <= 1
ORDER BY 
    StudentID, Rank;
