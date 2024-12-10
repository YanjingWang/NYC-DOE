-- You can add distinct ahead of studentID to find distinct StudentID
-- c. Check their grade changes compared to last year. Ideally, it should be one more than last year
SELECT 
    ts.StudentID,
    ts.CurrentGrade,
    ts.LastYearGrade,
    (ts.CurrentGradeInt - ts.LastYearGradeInt) AS GradeChange
FROM (
    SELECT 
        t.StudentID,
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
) ts
WHERE (ts.CurrentGradeInt - ts.LastYearGradeInt) != 1 --AND (ts.CurrentGradeInt - ts.LastYearGradeInt) !=0
ORDER BY GradeChange;

SELECT Gradelevel,BirthDate,AdmissionDTE, * FROM DWH_ATSStudents WHERE STUDENTID = 237107388;--NEW VALUE IS WRONG ATS ROLLOVER SIDE WRONG SOURCE USER ISSUE OR T5 ROLLVER ISSUE
select top 10 OFFICIAL_CLASS, SCHOOL_DBN as 'AdminDBN', ADMISSION_DTE, IEP_SPEC_ED_FLG,
STATUS, GRADE_LEVEL, SEX, SCHOOL_NUM, HOME_LANG, HISPANIC_FLG, BIRTH_DTE,  DISC_DTE as 'Discharge Date', DISC_CDE as 'Discharge Reason', * 
from [ATS_DEMO_Link].ATS_DEMO.[dbo].[BIOGDATA] where STUDENT_ID = '237107388'
--and STATUS = 'A' --active
--------------------------------------------------------------------------------------------------------------------------------------------
SELECT 
    ts.StudentID,
    ts.CurrentGrade,
    ts.LastYearGrade,
    (ts.CurrentGradeInt - ts.LastYearGradeInt) AS GradeChange
FROM (
    SELECT 
        t.StudentID,
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
) ts
WHERE (ts.CurrentGradeInt - ts.LastYearGradeInt) != 1 --AND (ts.CurrentGradeInt - ts.LastYearGradeInt) != 0  
ORDER BY GradeChange;
-------------------------------------------------------------------------------------------------------------
SELECT 
    ts.StudentID,
    ts.CurrentGrade,
    ts.LastYearGrade,
    (ts.CurrentGradeInt - ts.LastYearGradeInt) AS GradeChange
FROM (
    SELECT 
        t.StudentID,
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
) ts
WHERE (ts.CurrentGradeInt - ts.LastYearGradeInt) != 1 --AND (ts.CurrentGradeInt - ts.LastYearGradeInt) != 0
ORDER BY GradeChange;