-- Script that generates table for people who meet these criteria:
-- id, email, name, country(enumeration of US, TN and CO)
CREATE TABLE IF NOT EXISTS users(
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
