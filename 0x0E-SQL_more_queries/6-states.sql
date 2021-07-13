-- create a new database n table that stores eeuu states
-- create the database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- switch to the database
USE `hbtn_0d_usa`;
-- create table
CREATE TABLE IF NOT EXISTS `states` (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
