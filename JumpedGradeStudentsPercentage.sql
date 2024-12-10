-- CTE to get the most recent record for each student from BIOGDATA
WITH RecentCurrentGrades AS (
    SELECT 
        c.Student_ID,
        c.GRADE_LEVEL,
        ROW_NUMBER() OVER (PARTITION BY c.Student_ID ORDER BY c.ADMISSION_DTE DESC) AS rn
    FROM [ATS_DEMO_Link].[ATS_Demo].[dbo].[BIOGDATA] c
),

-- CTE to get the most recent record for each student from BIOGDATA_2023_2024
RecentLastYearGrades AS (
    SELECT 
        a.Student_ID,
        a.GRADE_LEVEL,
        ROW_NUMBER() OVER (PARTITION BY a.Student_ID ORDER BY a.ADMISSION_DTE DESC) AS rn
    FROM [ATS_DEMO_Link].[ATS_Support].[dbo].[BIOGDATA_2023_2024] a
),

-- CTE to map current grade levels to integers
CurrentGrades AS (
    SELECT 
        t.StudentID,
        c.GRADE_LEVEL AS CurrentGrade,
        CASE 
            WHEN c.GRADE_LEVEL = '0K' THEN 0
            WHEN c.GRADE_LEVEL = '01' THEN 1
            WHEN c.GRADE_LEVEL = '02' THEN 2
            WHEN c.GRADE_LEVEL = '03' THEN 3
            WHEN c.GRADE_LEVEL = '04' THEN 4
            WHEN c.GRADE_LEVEL = '05' THEN 5
            WHEN c.GRADE_LEVEL = '06' THEN 6
            WHEN c.GRADE_LEVEL = '07' THEN 7
            WHEN c.GRADE_LEVEL = '08' THEN 8
            WHEN c.GRADE_LEVEL = '09' THEN 9
            WHEN c.GRADE_LEVEL = '10' THEN 10
            WHEN c.GRADE_LEVEL = '11' THEN 11
            WHEN c.GRADE_LEVEL = '12' THEN 12
            ELSE NULL
        END AS CurrentGradeInt
    FROM RPT_StudentRegister t
    JOIN RecentCurrentGrades c ON t.StudentID = c.Student_ID
    WHERE c.rn = 1
),

-- CTE to map last year's grade levels to integers
LastYearGrades AS (
    SELECT 
        t.StudentID,
        a.GRADE_LEVEL AS LastYearGrade,
        CASE 
            WHEN a.GRADE_LEVEL = '0K' THEN 0
            WHEN a.GRADE_LEVEL = '01' THEN 1
            WHEN a.GRADE_LEVEL = '02' THEN 2
            WHEN a.GRADE_LEVEL = '03' THEN 3
            WHEN a.GRADE_LEVEL = '04' THEN 4
            WHEN a.GRADE_LEVEL = '05' THEN 5
            WHEN a.GRADE_LEVEL = '06' THEN 6
            WHEN a.GRADE_LEVEL = '07' THEN 7
            WHEN a.GRADE_LEVEL = '08' THEN 8
            WHEN a.GRADE_LEVEL = '09' THEN 9
            WHEN a.GRADE_LEVEL = '10' THEN 10
            WHEN a.GRADE_LEVEL = '11' THEN 11
            WHEN a.GRADE_LEVEL = '12' THEN 12
            ELSE NULL
        END AS LastYearGradeInt
    FROM RPT_StudentRegister t
    JOIN RecentLastYearGrades a ON t.StudentID = a.Student_ID
    WHERE a.rn = 1
),

-- Main CTE to calculate grade changes
GradeChanges AS (
    SELECT 
        cg.StudentID,
        (cg.CurrentGradeInt - lyg.LastYearGradeInt) AS GradeChange
    FROM CurrentGrades cg
    JOIN LastYearGrades lyg ON cg.StudentID = lyg.StudentID
)

-- Main query to calculate the percentage of students who jumped grade levels
SELECT 
    COUNT(*) AS TotalStudents,
    SUM(CASE WHEN GradeChange != 1 THEN 1 ELSE 0 END) AS JumpedGradeLevelStudents,
    (CAST(SUM(CASE WHEN GradeChange != 1 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*)) * 100 AS JumpedGradeLevelPercentage
FROM GradeChanges;
