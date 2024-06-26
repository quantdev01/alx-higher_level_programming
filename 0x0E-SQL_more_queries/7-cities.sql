-- CREate cities db
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- creating the table
CREATE TABLE IF NOT EXISTS cities
(
        id INT PRIMARY KEY AUTO_INCREMENT,
		state_id INT,
		FOREIGN KEY (state_id) REFERENCES states(id),
        name VARCHAR(256) NOT NULL
);
