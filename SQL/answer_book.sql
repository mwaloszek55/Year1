
-- =================================================
--   CS1106/CS6503 Test -- Wednesday, 18 Nov 2020
-- =================================================

-- Your Name: Mateusz Waloszek 
-- Your Id: 120412764

-- =================================================
-- QUESTION 1: Place SQL below the dashed line
-- -------------------------------------------------
SELECT first_name, last_name
FROM persons
WHERE first_name LIKE "%r%" OR last_name LIKE "%r%";
-- =================================================
-- QUESTION 2: Place SQL below the dashed line
-- -------------------------------------------------
SELECT county, COUNT(*) as "nmbr of ppl"
FROM persons
GROUP BY county
ORDER BY county;
-- =================================================
-- QUESTION 3: Place SQL below the dashed line
-- -------------------------------------------------
SELECT DISTINCT first_name
FROM likes as l JOIN persons as p
ON l.person_id=p.person_id
WHERE food LIKE "%e%";
-- =================================================
-- QUESTION 4: Place SQL below the dashed line
-- -------------------------------------------------
SELECT p.first_name, p.last_name
FROM knows as k JOIN persons as p
ON k.person_id=p.person_id
WHERE k.friend_id="345678";
-- =================================================
-- QUESTION 5: Place SQL below the dashed line
-- -------------------------------------------------
SELECT first_name
FROM persons
EXCEPT
SELECT p.first_name
FROM knows as k JOIN persons as p
ON k.person_id=p.person_id
WHERE k.friend_id="345678" OR (p.first_name="Aoife" AND p.last_name="Ahern");
-- =================================================
-- QUESTION 6: Place SQL below the dashed line
-- -------------------------------------------------
SELECT DISTINCT p.first_name, p.last_name
FROM knows as k JOIN persons as p
ON k.person_id=p.person_id
WHERE k.friend_id="345678" AND k.friend_id="986347";
-- =================================================
-- QUESTION 7: Place SQL below the dashed line
-- -------------------------------------------------
SELECT DISTINCT first_name
FROM persons 
WHERE birth_date =(SELECT MIN(birth_date) FROM persons)
OR birth_date =(SELECT MAX(birth_date) FROM persons);
-- =================================================
-- QUESTION 8: Place SQL below the dashed line
-- -------------------------------------------------
SELECT food, COUNT(*)
FROM likes JOIN persons
ON likes.person_id=persons.person_id
WHERE county="Cork"
GROUP BY food
HAVING COUNT(*)
ORDER BY COUNT(*) DESC;
-- =================================================
-- QUESTION 9: Place SQL below the dashed line
-- -------------------------------------------------
SELECT county, COUNT(*)
FROM persons as p JOIN likes as l
ON p.person_id=l.person_id
AND p.person_id < l.person_id
GROUP BY county
HAVING COUNT(*);
-- =================================================
-- QUESTION 10: Place SQL below the dashed line
-- -------------------------------------------------
SELECT DISTINCT *
FROM persons as p1 JOIN persons as p2
ON p1.person_id=p2.person_id;


SELECT DISTINCT p1.first_name, p2.first_name
FROM persons as p1 JOIN persons as p2
ON p1.person_id=p2.person_id
WHERE substr(p2.first_name, 0, 1) = substr(p1.first_name, 0, 1);

