CREATE TABLE jobs (
	id SERIAL PRIMARY KEY,
	jobtitle TEXT NOT NULL,
	company TEXT NOT NULL,
	locations TEXT NOT NULL,
	about Text NOT NULL,
	description TEXT,
	requirements TEXT NOT NULL,
	typ TEXT NOT NULL,
	industry TEXT NOT NULL,
	salary DOUBLE PRECISION NOT NULL,
	dat INT NOT NULL
	);