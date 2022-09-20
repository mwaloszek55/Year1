-- Q2
/* 
CREATE TABLE reviews
(
    ID INT,
    name VARCHAR(30),
    city CHAR(15),
    country CHAR(15),
    date_last_reviewed DATE,
    category INT,
    rating REAL,
    PRIMARY KEY (ID)

);

INSERT INTO reviews
(ID, name, city, country, date_last_reviewed, category, rating)
VALUES 
('1', 'Nikita''s Hell''s Kitchen', 'Dublin', 'Ireland', '2019/07/05', '4', '10'),
('2', 'Dinano''s', 'Tralee', 'Ireland', '2017/01/01', '5', '5'),
('3', 'Crabbie''s', 'Moscow', 'Russia', '2019/12/25', '6', '1');


SELECT *
FROM reviews;



DELETE FROM reviews
WHERE rating < 4.0;


SELECT *
FROM reviews;


UPDATE reviews
SET rating = rating * 1.05
WHERE rating < 6.0 AND date_last_reviewed >= 2017/01/01;

SELECT *
FROM reviews;

SELECT name
FROM reviews
WHERE city='Dublin' AND rating > 7.5 AND (category = 4 OR category = 3);



SELECT name, category, rating
FROM reviews
WHERE city='Cork'
ORDER BY category DESC, rating DESC;
*/


--Q3

SELECT *
FROM hotels;

SELECT *
FROM rooms;



/*SELECT *
FROM hotels
WHERE city='Dublin' AND hotel_num IN
    (SELECT hotel_num
    FROM rooms
    WHERE room_type='double' AND price BETWEEN 100 AND 200);



SELECT *
FROM hotels
WHERE city='Galway' AND hotel_num IN
    (SELECT hotel_num
    FROM rooms
    WHERE room_type='single' AND price>250);*/




SELECT *
FROM bookings;

SELECT *
FROM guests;




/*SELECT h.hotel_name, b.arr_date, b.dep_date
FROM hotels as h
    JOIN bookings as b
ON 
h.hotel_num=b.hotel_num
WHERE h.city='Cork' AND strftime('%m', b.arr_date) = '07' AND strftime('%Y', b.arr_date) = '2018'
AND b.guest_num IN
    (SELECT guest_num
    FROM guests
    WHERE guest_name='Trump, Donald')
ORDER BY b.arr_date ASC;*/


/*SELECT COUNT(r.room_num) as 'number of rooms', AVG(r.price) as 'average price'
FROM hotels as h
    JOIN rooms as r
ON 
h.hotel_num=r.hotel_num
WHERE r.room_type='single'
GROUP BY h.city
HAVING COUNT(r.room_num)=1000
ORDER BY COUNT(r.room_num) DESC;*/




SELECT h.hotel_name, r.price, r.room_num
FROM hotels as h
    JOIN rooms as r
ON 
h.hotel_num=r.hotel_num
WHERE h.city='Galway' AND r.room_type='double'
EXCEPT
SELECT h.hotel_name, r.price, r.room_num
FROM hotels as h
    JOIN rooms as r
ON 
h.hotel_num=r.hotel_num
WHERE r.hotel_num IN
    (SELECT hotel_num
    FROM bookings
    WHERE arr_date='2017-12-31');




















