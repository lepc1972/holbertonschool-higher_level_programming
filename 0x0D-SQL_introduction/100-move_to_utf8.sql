-- convert  database to UTF-8 character set n collation

-- use database
USE hbtn_0c_0;

-- change the database defaults settings
ALTER DATABASE CHARACTER SET utf8mb4;
ALTER DATABASE COLLATE utf8mb4_unicode_ci;

-- change the table default
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
