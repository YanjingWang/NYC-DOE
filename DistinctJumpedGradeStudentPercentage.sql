-- Below query use distinct student counts / total students from RPT_StudentRegister table to calculated percentage, jumped gradelevel also contain 0 
-- Calculate the count of students who have jumped a grade level
WITH JumpedGradeLevel AS (
    SELECT 
        DISTINCT t.StudentID,
        c.GradeLevel AS CurrentGrade,
        a.GradeLevel AS LastYearGrade,
        CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS CurrentGradeInt,
        CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS LastYearGradeInt
    FROM RPT_StudentRegister t
    JOIN RPT_ParaServicesLinkage c ON t.StudentID = c.StudentID
    JOIN [arch].RPT_ParaServicesLinkage_SY24 a ON t.StudentID = a.StudentID
    WHERE (CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END - CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END) != 1 
)
-- Calculate the total number of students
SELECT 
    COUNT(*) AS DistinctJumpedGradeLevelCount,
    (SELECT COUNT(*) FROM RPT_StudentRegister) AS TotalStudentCount,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM RPT_StudentRegister)) AS PercentageJumpedGradeLevel
FROM JumpedGradeLevel;

----------------------------------------------------------------------------------------------------
WITH JumpedGradeLevel AS (
    SELECT 
        DISTINCT t.StudentID,
        c.GradeLevel AS CurrentGrade,
        a.GradeLevel AS LastYearGrade,
        CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS CurrentGradeInt,
        CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS LastYearGradeInt
    FROM RPT_StudentRegister t
    JOIN RPT_RelatedServicesLinkage c ON t.StudentID = c.StudentID
    JOIN [arch].RPT_RelatedServicesLinkage_SY24 a ON t.StudentID = a.StudentID
    WHERE (CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END - CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END) != 1 
)
-- Calculate the total number of students
SELECT 
    COUNT(*) AS DistinctJumpedGradeLevelCount,
    (SELECT COUNT(*) FROM RPT_StudentRegister) AS TotalStudentCount,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM RPT_StudentRegister)) AS PercentageJumpedGradeLevel
FROM JumpedGradeLevel;
--------------------------------------------------------------------------------------------------
WITH JumpedGradeLevel AS (
    SELECT 
        DISTINCT t.StudentID,
        c.GradeLevel AS CurrentGrade,
        a.GradeLevel AS LastYearGrade,
        CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS CurrentGradeInt,
        CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END AS LastYearGradeInt
    FROM RPT_StudentRegister t
    JOIN RPT_RelatedServicesSummer c ON t.StudentID = c.StudentID
    JOIN [arch].RPT_RelatedServicesSummer_SY24 a ON t.StudentID = a.StudentID
    WHERE (CASE 
            WHEN c.GradeLevel = '0K' THEN 0
            WHEN c.GradeLevel = '01' THEN 1
            WHEN c.GradeLevel = '02' THEN 2
            WHEN c.GradeLevel = '03' THEN 3
            WHEN c.GradeLevel = '04' THEN 4
            WHEN c.GradeLevel = '05' THEN 5
            WHEN c.GradeLevel = '06' THEN 6
            WHEN c.GradeLevel = '07' THEN 7
            WHEN c.GradeLevel = '08' THEN 8
            WHEN c.GradeLevel = '09' THEN 9
            WHEN c.GradeLevel = '10' THEN 10
            WHEN c.GradeLevel = '11' THEN 11
            WHEN c.GradeLevel = '12' THEN 12
            ELSE NULL
        END - CASE 
            WHEN a.GradeLevel = '0K' THEN 0
            WHEN a.GradeLevel = '01' THEN 1
            WHEN a.GradeLevel = '02' THEN 2
            WHEN a.GradeLevel = '03' THEN 3
            WHEN a.GradeLevel = '04' THEN 4
            WHEN a.GradeLevel = '05' THEN 5
            WHEN a.GradeLevel = '06' THEN 6
            WHEN a.GradeLevel = '07' THEN 7
            WHEN a.GradeLevel = '08' THEN 8
            WHEN a.GradeLevel = '09' THEN 9
            WHEN a.GradeLevel = '10' THEN 10
            WHEN a.GradeLevel = '11' THEN 11
            WHEN a.GradeLevel = '12' THEN 12
            ELSE NULL
        END) != 1 
)
-- Calculate the total number of students
SELECT 
    COUNT(*) AS DistinctJumpedGradeLevelCount,
    (SELECT COUNT(*) FROM RPT_StudentRegister) AS TotalStudentCount,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM RPT_StudentRegister)) AS PercentageJumpedGradeLevel
FROM JumpedGradeLevel;
