-- creates a table called first_table in the current database in the MySQL server
-- the columns are: id INT, name VARCHAR(256). doesn't fail if table already exists

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
