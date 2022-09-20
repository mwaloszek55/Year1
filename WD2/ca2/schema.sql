DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);


DROP TABLE IF EXISTS scores;

CREATE TABLE scores
(
    user_id TEXT,
    score INT
);

SELECT *
from scores;