CREATE TABLE student (
  INTEGER PRIMARY KEY AUTOINCREMENT id,
  TEXT "name",
  TEXT "lastname",
  TEXT UNIQUE "email",
  INTEGER UNIQUE phone
);
