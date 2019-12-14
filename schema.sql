DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INTEGER PRIMARY KEY autoincrement,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	last_alert_check INTEGER NOT NULL
);

DROP TABLE IF EXISTS alerts;
CREATE TABLE alerts (
	id INTEGER PRIMARY KEY autoincrement,
	user_id INTEGER NOT NULL,
	alert TEXT NOT NULL	
);
