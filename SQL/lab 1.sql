SELECT * 
FROM students;


-- SELECT first_name, last_name
-- FROM students;



-- SELECT first_name, last_name
-- FROM students
-- ORDER BY points;

-- SELECT DISTINCT hometown
-- FROM students;

-- SELECT first_name
-- FROM students
-- WHERE points >= 450;

-- SELECT first_name
-- FROM students
-- WHERE points = 525;

-- SELECT first_name, last_name
-- FROM students
-- WHERE points <> 525;


-- SELECT first_name, last_name
-- FROM students
-- WHERE points BETWEEN 400 AND 500;



-- SELECT first_name, last_name
-- FROM students
-- WHERE hometown="Cork";


-- SELECT first_name
-- FROM students
-- WHERE date_of_birth = '1993-01-25';



-- SELECT first_name, last_name
-- FROM students
-- WHERE date_of_birth <= '1992-01-01';


--SELECT first_name
--FROM students
--WHERE date_of_birth = '1994-12-25';

--SELECT ALL *
--FROM students
--WHERE first_name = 'Ciara';

--SELECT ALL *
--FROM students
--WHERE first_name = 'ciara';

--SELECT ALL *
--FROM students
--WHERE first_name OR last_name = 'Barry';

--SELECT ALL *
--FROM students
--WHERE last_name = 'O’Kelly';

--SELECT *
--FROM students
--WHERE date_of_birth >= '1994-01-01 00:00:00' 
  --  AND date_of_birth < '1995-01-01 00:00:00';

--SELECT first_name, hometown
--FROM students
--WHERE id_number = '112345678'
 --   OR id_number = '112356489';



--SELECT *
--FROM students
--WHERE course = 'ck401' OR 'ck402';

--SELECT *
--FROM students
--WHERE points >= '450' AND hometown = 'Cork';

/*SELECT *
FROM students
WHERE last_name < 'Cuddihy';

SELECT *
FROM students
WHERE last_name <= 'Callaghan'
    AND first_name < 'Harry';*/


SELECT *
FROM students
WHERE last_name LIKE 'C%';


/*SELECT last_name AS 'Surname', 
first_name AS 'Given Name(s)', 
points AS 'CAO Points'
FROM students
WHERE points>='450'
ORDER BY first_name DESC;


--SELECT hometown, SUM(points)
--FROM students
--GROUP BY hometown
--ORDER BY points DESC;

