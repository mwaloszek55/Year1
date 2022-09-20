CREATE TABLE reviews
(
    ID INT,
    name VARCHAR(30),
    city CHAR(15),
    country CHAR(15),
    date_last_reviewed DATE,
    category INT,
    rating REAL,
    rating_review VARCHAR(255),
    PRIMARY KEY (ID)

);

INSERT INTO reviews
(ID, name, city, country, date_last_reviewed, category, rating, rating_review)
VALUES 
('1', 'Nikita''s Hell''s Kitchen', 'Tralee', 'Ireland', '2019/07/05', '4', '10', 'The food..it''s actually exquisite, this Nikita guy knows what the fuck is up.'),
('2', 'Dinano''s', 'Tralee', 'Ireland', '2018/10/30', '5', '5', 'It''s...okay.'),
('3', 'Crabbie''s', 'Moscow', 'Russia', '2019/12/25', '6', '1', 'Not the type of crabs I was looking for.'),
('4', 'Black''s', 'Cape Town', 'South Africa', '2020/04/04', '1', '3', 'Weirdly a lot of white people.'),
('5', 'Bubby''s', 'Wuhan', 'China', '2020/01/01', '3', '8', 'The bat soup was...alrighty.'),
('6', 'Pluggy''s', 'Detroit', 'USA', '2009/12/25', '1', '0', 'The neighbourhood was troubling.'),
('7', 'Sabby''s', 'Delhi', 'India', '2018/03/13', '3', '7', 'The sheikh chef shook.'),
('8', 'Raja''s Kebab House', 'Dublin', 'Ireland', '2020/02/25', '3', '8', 'Legendary');

/*DELETE FROM reviews
WHERE rating<4;*/

UPDATE reviews
SET rating = rating+2
WHERE date_last_reviewed>'2020/01/01' AND rating<'6';


SELECT *
FROM reviews;

SELECT name, city, country, rating, category
FROM reviews
WHERE city='Dublin' AND rating>='7.5' 
AND category>'2' AND category<'5';

SELECT name, category, rating
FROM reviews
WHERE country='Ireland'
ORDER BY category DESC;

SELECT name, category, rating
FROM reviews
WHERE country='Ireland'
ORDER BY rating DESC;


