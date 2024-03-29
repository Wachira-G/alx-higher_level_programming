-- creates the database hbtn_0d_usa and the table cities (database hbtn_0d_usa)
-- cities: id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null, must be a FOREIGN KEY to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (state_id) REFERENCES states(id)
);
