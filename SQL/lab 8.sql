SELECT *
FROM hotels;

---SELECT *
--FROM hotels
--WHERE city='Cork';

SELECT *
FROM guests;

/*SELECT guest_name, guest_address
FROM guests
WHERE guest_address LIKE '%Limerick';

SELECT *
FROM rooms;

SELECT room_num as id
FROM rooms
WHERE price<70 AND room_type='double';*/

SELECT *
FROM bookings;

SELECT *
FROM rooms;

--SELECT *
--FROM bookings
--WHERE dep_date=NULL;



--SELECT COUNT(hotel_num) as 'Number of Hotels'
--FROM hotels;

--Question 6 (unfinished)
SELECT h.hotel_num, COUNT(r.room_num)
FROM hotels as h
JOIN rooms as r
ON h.hotel_num=r.hotel_num
WHERE r.price<70
GROUP BY h.hotel_num
ORDER BY h.hotel_num;





/*
SELECT COUNT(*)
FROM rooms
WHERE hotel_num IN
    (SELECT hotel_num
    FROM hotels
    WHERE hotel_num IN
        (SELECT hotel_num
        FROM rooms
        WHERE price<70)
GROUP BY hotel_num
HAVING COUNT(*)
    );

SELECT COUNT(*)
FROM rooms
WHERE hotel_num IN
    (SELECT hotel_num
    FROM hotels
    WHERE hotel_name='Hotel Splendide')
GROUP BY hotel_num
HAVING COUNT(*);*/



/*SELECT COUNT(hotel_name) as 'Number of Hotels'
FROM hotels
WHERE hotel_num IN
    (SELECT hotel_num
    FROM rooms
    WHERE price<70 AND room_type='double');



SELECT AVG(price) as 'Average Price'
FROM rooms;

SELECT AVG(price) as 'Average Price in Cork'
FROM rooms
WHERE hotel_num IN
    (SELECT hotel_num
    FROM hotels
    WHERE city='Cork');


SELECT AVG(price) as 'Average Price in Cork'
FROM rooms
WHERE hotel_num IN
        (SELECT hotel_num
        FROM rooms
        WHERE price<70 AND room_type='double');*/



/*SELECT AVG(price) as 'Average Price for double rooms in Cork'
FROM rooms
WHERE room_type='double' AND hotel_num IN
    (SELECT hotel_num
    FROM hotels
    WHERE city='Cork');


SELECT COUNT(*)
FROM bookings
WHERE arr_date LIKE '%11%'
GROUP BY hotel_num;


SELECT price, room_type
FROM rooms
WHERE hotel_num IN
    (SELECT hotel_num
    FROM hotels
    WHERE hotel_name='Hotel Splendide');*/


SELECT h.hotel_name, COUNT(r.room_num) as 'number of rooms'
FROM hotels as h
JOIN rooms as r
ON h.hotel_num=r.hotel_num
WHERE h.city='Galway';




SELECT DISTINCT h1.hotel_name, h2.hotel_name
FROM hotels as h1
JOIN hotels as h2
ON h1.hotel_num=h2.hotel_num;


































































