-- write a script that creates a table in a database
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
