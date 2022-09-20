DROP TABLE IF EXISTS gigs;

CREATE TABLE gigs 
(
    gig_id INTEGER PRIMARY KEY AUTOINCREMENT,
    band TEXT NOT NULL,
    gig_date TEXT NOT NULL
);

INSERT INTO gigs (band, gig_date)
VALUES ('Decaying Shroom', '2021-01-12'),
       ('Belated Tonic', '2021-01-14'),
       ('Dumpy Tension of the Divided Unicorn', '2021-02-10'),
       ('Belated Tonic', '2021-02-20'),
       ('Missing Roller and the Earl', '2021-02-26'),
       ('Glam Blizzard', '2021-03-07'),
       ('Piscatory Classroom', '2021-03-12'),
       ('Prickly Muse', '2021-03-20'),
       ('Interactive Children of the Phony Filth', '2021-03-29');



DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);