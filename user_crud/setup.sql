CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- Creating some default test users:
INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "Gary",
     "Rapoza",
     "Golf"
 );

 INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "John",
     "Lennon",
     "Skydiving"
 );

 INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "Jannis",
     "Joplin",
     "Music"
 );

 UPDATE user (
     first_name,
     last_name,
     hobbies
 )