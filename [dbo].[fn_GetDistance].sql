USE [SEO_MART]
GO

/****** Object:  UserDefinedFunction [dbo].[fn_GetDistance]    Script Date: 12/9/2024 9:55:29 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO




CREATE   function [dbo].[fn_GetDistance] 
(
	@FrmLatitude Float,
	@FrmLongitude Float,
	@ToLatitude Float,
	@ToLongitude Float
)
Returns float

/**************************************************************************************************************************************************************************
Object Name: 
Sample call: Select dbo.fn_GetDistance(@,@,@,@,@)
Purpose: Get Case Type value.  
Date Created: 

Modification Details:
Author				ModifiedDate		Comments
Christopher Agwu	2/15/2023			Initial
***************************************************************************************************************************************************************************/

As
Begin
	Declare @GetDistance Float;
	Declare @FromPoint Varchar(200), @ToPoint Varchar(200)

	IF @ToLatitude IS NULL OR @ToLongitude IS NULL OR @FrmLatitude IS NULL OR @FrmLongitude IS NULL
	BEGIN
		SET @GetDistance=NULL;
		Return @GetDistance;
	END;

	SET @FromPoint=CONCAT('POINT(',ISNULL(@FrmLongitude,0),' ', ISNULL(@FrmLatitude,0),')')
	SET @ToPoint=CONCAT('POINT(',ISNULL(@ToLongitude,0),' ',ISNULL(@ToLatitude,0),')')
	
	DECLARE @MetersPerMile FLOAT = 1609.344;
	DECLARE @fromGeog GEOGRAPHY = GEOGRAPHY::STGeomFromText(@FromPoint, 4326);
	DECLARE @toGeog GEOGRAPHY = GEOGRAPHY::STGeomFromText(@ToPoint, 4326);
	SET @GetDistance = @fromGeog.STDistance(@toGeog)/@MetersPerMile;
	
	IF @GetDistance=0
		SET @GetDistance=0.001;

	Return @GetDistance;
End

GO


