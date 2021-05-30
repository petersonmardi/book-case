#IF EXISTS DROP student;

CREATE TABLE student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "lastname" TEXT,
  "email" TEXT UNIQUE,
  phone INTEGER UNIQUE
);
