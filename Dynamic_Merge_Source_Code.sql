USE [D496IDS_DEV]
USE [D496IDS_ARCH]
DECLARE @dst NVARCHAR(1000) = '[D496IDS_ARCH].[APD_IDS].[TACCOUNT]'
DECLARE @src NVARCHAR(1000) = '[D496IDS_DEV].[APD_IDS].[TACCOUNT]'
DECLARE @eqPK NVARCHAR(1000) 
DECLARE @neColumns NVARCHAR(max)
DECLARE @updColumns NVARCHAR(max)
DECLARE @insColumn NVARCHAR(max) 
DECLARE @srcColumns NVARCHAR(max)
DECLARE @dstPrimaryKeys TABLE ([name] sysname)

INSERT INTO @dstPrimaryKeys SELECT c.name FROM sys.indexes i 
INNER JOIN sys.index_columns ic on ic.object_id = i.object_id AND ic.index_id = i.index_id
INNER JOIN sys.columns c on c.object_id = i.object_id and c.column_id = ic.column_id
WHERE i.is_primary_key = 1 and i.object_id = object_id(@dst)

SELECT @eqPK = COALESCE(@eqPK + ' AND ', '') + 't.' + name + '=' + 's.' + name FROM @dstPrimaryKeys
--print @eqPK

SELECT @updColumns = COALESCE(@updColumns + ',', '') + 't.' + name + '=' + 's.' + name
FROM sys.columns WHERE object_id = object_id(@dst) AND name NOT IN (SELECT name FROM @dstPrimaryKeys) and name = 'SfdcAccountIdNumber'
--print @updColumns

SET @neColumns = Replace(Replace(@updColumns, ',', ' OR '), '=', '<>')
--print @neColumns

SELECT @insColumn = COALESCE(@insColumn + ',', '') + name 
FROM sys.columns WHERE object_id = object_id(@dst) and name IN('AccountSystemNumber','SfdcAccountIdNumber')
--print @insColumn

SELECT @srcColumns = COALESCE(@srcColumns + ',', '') + 's.' + name
FROM sys.columns WHERE object_id = object_id(@dst) and name IN('AccountSystemNumber','SfdcAccountIdNumber')
--print @srcColumns


DECLARE @tsql nvarchar(max) = 
'SET IDENTITY_INSERT ' + @dst + ' ON;' +
'MERGE ' + @dst + ' AS t ' +
'USING ' + @src + ' AS s ' +
'ON (' + @eqPK + ') ' +
'WHEN MATCHED AND ' + @neColumns + ' THEN ' +
'UPDATE SET ' + @updColumns + 
' WHEN NOT MATCHED BY TARGET THEN INSERT (' + @insColumn + ') ' +
'VALUES (' + @srcColumns + ') ' +
'WHEN NOT MATCHED BY SOURCE THEN DELETE;'

PRINT @tsql
EXEC sp_executesql @tsql

SELECT * FROM [D496IDS_DEV].[APD_IDS].[TACCOUNT]
SELECT * FROM [D496IDS_ARCH].[APD_IDS].[TACCOUNT]