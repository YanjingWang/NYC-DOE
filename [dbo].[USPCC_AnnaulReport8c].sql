USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport8c]    Script Date: 11/12/2024 3:13:53 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





/************************************************************************************************************************************************************************
Object Name: dbo.USPCCAnnaulReport8c
Purpose:	This procedure returns data for City Council Annaul Report c "SWDs by School"
	SWD = Students with Disabilities
	This particular annual report is based off of June 15th snapshot.
	While city council annual reports are usually based off on June 30th (end of year) snapshots, 
	for this report we use 6/15. Reason: Schools may discharge students early (between June 20th and June 29th).
	It's safe to assume that any student who was active till 6/15 to have completed the school year.

	Python program will call this stored procedure to generate the Excel Report for CC annual report

Date Created: 10/23/2023
Modification Details:

Author			ModifiedDate		Comments
Raji Munnangi	10/23/2023			Initial version
Charlotte Wang   11/09/2023          Final Version
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART
***************************************************************************************************************************************************************************/
CREATE procedure [dbo].[USPCC_AnnaulReport8c]
	@tableName varchar(100) = ''
as
begin
	
	if isnull(@tableName, '') = ''
	begin
		declare @currYear_YY char(2)
		set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
		set @tableName = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 

	declare @sql nvarchar(max) = ''
	select @sql = 
	' select  EnrolledDBN as [School DBN], count(studentID) as [Students with IEPs]  ' + 
	' FROM SEO_MART.snap.' + @tableName + -- CC_StudentRegisterR814_061523
	' group by EnrolledDBN ' +
	' order by EnrolledDBN '

	exec(@sql)

end 
 
GO


