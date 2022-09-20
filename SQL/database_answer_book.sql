-- ADD YOUR NAME AND ID NUMBER BELOW
-- =================================
-- Name: Mateusz Waloszek
-- Id: 120412764
 
-- QUESTION ONE
-- ============
-- 
-- Submit your answer seperately as a scanned image.
-- 
-- QUESTION TWO
-- ============
-- Include your answers to the various parts in the appropriate sections below.
 
-- Part (i)
-- --------

CREATE TABLE trips
(
    ID INT,
    title VARCHAR(30),
    dep_date DATE,
    length INT,
    places INT,
    price REAL,
    PRIMARY KEY (ID)

);

-- Part (ii)
-- ---------

INSERT INTO trips
(ID, title, dep_date, length, places, price)
VALUES 
('1', 'Treasures of Sicily', '2019-05-25', '6', '3', '100.50'),
('2', 'Adventures of Copenhagen', '2020-07-13', '5', '5', '5000.00'),
('3', 'Endeavors in Moscow', '2018-03-17', '4', '10', '10000.00');

-- Part (iii)
-- ----------
DELETE FROM trips
WHERE dep_date LIKE '2020-07-%%';
-- Part (iv)
-- ---------
/*
The database might be enhanced by adding new tables. 
One of the tables added would be "customers".
In this table i would record the customers names, addresses, and some form of id as attributes to the table, the ids are to distinguish different customers in relation to their booking.
I would add another table called "bookings". 
In this table I would add the booking date, the ids of customers and the ids of the trips booked as attributes to the table, this way i can track which customer booked which patricular trip.
*/

-- QUESTION THREE
-- ==============
-- Include your answers to the various parts in the appropriate sections below.
-- 
-- Part (i)
-- --------
SELECT region, sum(surface_area), min(name), max(name)
FROM countries
GROUP BY region
HAVING COUNT(name) > 5;
-- Part (ii)
-- ---------
SELECT c1.name
FROM cities as c1
    JOIN countries as c2
ON 
c1.country_code=c2.code
WHERE c1.population >= 5000000
ORDER BY c2.continent, c2.name, c1.population DESC;
-- Part (iii)
-- ----------
SELECT c1.name
FROM cities as c1
    JOIN countries as c2
ON 
c1.country_code=c2.code
GROUP BY c2.name
HAVING max(c1.population);
-- Part (iv)
-- ---------
SELECT c1.language, c1.percentage
FROM country_languages as c1
    JOIN countries as c2
ON c1.country_code=c2.code;

-- Part (v)
-- ----------
SELECT head_of_state, name
FROM countries
WHERE head_of_state IN
    (SELECT head_of_state
    FROM countries
    GROUP BY head_of_state
    HAVING COUNT(name) > 1);

-- Part (vi)
-- ---------

SELECT name
FROM countries 
WHERE indep_year = 
    (SELECT MIN(indep_year)
    FROM countries
    WHERE code IN
        (SELECT country_code
        FROM country_languages
        WHERE language='English'
        AND (is_official='T' OR percentage>50))
    );





