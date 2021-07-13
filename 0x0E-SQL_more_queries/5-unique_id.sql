-- create a table with id unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
