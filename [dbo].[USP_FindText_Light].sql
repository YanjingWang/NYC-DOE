USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USP_FindText_Light]    Script Date: 12/9/2024 9:44:03 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USP_FindText_Light] (@pText varchar(80))

 as
/*************************************************************************************************
Object Name:	  SEO_FindText
Purpose:		Find the text in stored code blocks (procedure, view, function)
Execute example: exec dbo.USP_FindText_Light 'Duration'
				 exec dbo.USP_FindText_Light @pText = 'Duration'	-- to find Duration
				 exec dbo.USP_FindText_Light @pText = '''T5CAP'''-- to find 'T5CAP' (with text having single quotes around T5CAP)
				 -- Use Escape chars in Brackets [] like [%] to find percent char; to find text with ' replace each with ''
Modification Details:
Author		ModifiedDate		Comments
------		------------		-------------------
SergeyG		05/15/2023			Initial (light, without statistics)
**************************************************************************************************/

begin
    SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED 
    SET NOCOUNT ON
	declare @vReturnLen				INT 
    declare @vSearchString			VARCHAR(MAX); --	declare @OverrideSearchStringWith VARCHAR(MAX) - option is not used
    SET @vSearchString = @pText
    SET @vReturnLen	= 50;
/*
    with LastRun	as (select OBJECT_ID, MAX(last_execution_time) as LastRun
						  from sys.dm_exec_procedure_stats
						 group by object_id
						)
*/
        SELECT  db_name() DBName, OL.Type, OBJECT_NAME(OL.Obj_ID) AS 'Name'
				,LTRIM(RTRIM(REPLACE(SUBSTRING(REPLACE(OBJECT_DEFINITION(OL.Obj_ID), NCHAR(0x001F), ''), CHARINDEX(@vSearchString, OBJECT_DEFINITION(OL.Obj_ID)) - @vReturnLen, @vReturnLen * 2), @vSearchString, '   ***-->>' + @vSearchString + '<<--***  '))) AS SourceLine
				,CAST(REPLACE(REPLACE(REPLACE(REPLACE(CONVERT(VARCHAR(MAX), REPLACE(OBJECT_DEFINITION(OL.Obj_ID), NCHAR(0x001F), '')), '&', '(A M P)'), '<', '(L T)'), '>', '(G T)'), @vSearchString, '<!-->' + @vSearchString + '<-->') AS XML) AS 'SearchedText'
        --		,(SELECT [processing-instruction(A)] = REPLACE(OBJECT_DEFINITION(OL.Obj_ID), NCHAR(0x001F), '') FOR	XML PATH(''), TYPE )	AS 'Code' -- adds tags
				,ModDt					AS Modified
--				,LastRun					AS LastRun
        FROM    (SELECT (CASE o.type
                          WHEN 'P' THEN 'Proc'
                          WHEN 'V' THEN 'View'
                          WHEN 'TR' THEN 'Trig'
                          ELSE 'Func'
							END)		AS 'Type'
                       , o.OBJECT_ID	AS OBJ_id
                       , o.modify_Date	AS ModDt
--						, R.LastRun
				   FROM sys.Objects O WITH (NOLOCK)
--				   LEFT 
--				   join LastRun		R	on o.object_id = R.object_id
                  WHERE OBJECT_DEFINITION(o.OBJECT_ID) LIKE '%' + @vSearchString + '%'
                        AND o.type IN ('P', 'V', 'TR', 'FN', 'IF', 'TF')
                     --   AND R.LastRun  IS NOT null	-- uncomment to pick only recently used (log is yet present)
                ) OL
		order by 1,2,3
    OPTION  (FAST 10)

end
GO


