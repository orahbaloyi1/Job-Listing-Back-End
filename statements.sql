CREATE TABLE jobs (
	id SERIAL PRIMARY KEY,
	slug TEXT NOT NULL,
	jobtitle TEXT NOT NULL,
	company TEXT NOT NULL,
	about TEXT NOT NULL,
	description TEXT NOT NULL,
	requirements TEXT NOT NULL,
	jobtype TEXT NOT NULL,
	location TEXT NOT NULL,
	industry TEXT NOT NULL,
	salary INT NULL
	);
	
	CREATE TABLE userEmail (
	id SERIAL PRIMARY KEY,
	emailaddress TEXT NOT NULL);