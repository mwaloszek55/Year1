SELECT *
FROM persons;

SELECT *
FROM likes;

/* SELECT first_name
FROM persons
WHERE first_name LIKE 'A%';

SELECT first_name
FROM persons
WHERE first_name LIKE '%A';

SELECT first_name
FROM persons
WHERE first_name LIKE '%A%';

SELECT first_name
FROM persons
WHERE first_name LIKE '_____';

SELECT first_name
FROM persons
WHERE street LIKE '%Street%';

SELECT food
FROM likes
WHERE food LIKE '% %';

SELECT food
FROM likes
WHERE food LIKE '%te%';

SELECT *
FROM persons as p
CROSS JOIN likes as l
on p.person_id=l.person_id;

SELECT first_name, food
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id;

SELECT food
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE first_name='Aoife' AND last_name='Ahern';

SELECT first_name, food
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE county='Cork';

SELECT DISTINCT food
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE gender='F'; 

SELECT DISTINCT town
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE food='Beer';


SELECT first_name, food
FROM persons as p
CROSS JOIN likes as l
on p.person_id=l.person_id;

SELECT p1.food, p2.food
FROM likes as p1
CROSS JOIN likes as p2
ON p1.food=p2.food; 

SELECT *
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id;

SELECT p.person_id
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE food='Pizza' AND food='Nutella';

SELECT p.person_id
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE food='Pizza' OR food='Nutella'
OR food='Pizza' AND food='Nutella';


SELECT first_name
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE county='Cork' AND food='Beer';

SELECT first_name
FROM persons AS p 
JOIN likes AS f 
ON p.person_id=f.person_id
WHERE food='Pizza' AND food='Nutella';

SELECT p1.first_name, p2.first_name
FROM persons as p1
CROSS JOIN persons as p2;


SELECT p1.first_name, p2.first_name
FROM persons as p1
CROSS JOIN persons as p2
ON p1.first_name=p2.first_name; */

SELECT first_name
FROM persons
GROUP BY birth_date HAVING COUNT(*)>1;

SELECT COUNT(first_name) AS count, food
FROM persons as p1
CROSS JOIN likes as p2
ON p1.person_id=p2.person_id
GROUP BY p2.food;

SELECT *
FROM persons AS p1
JOIN likes AS p2
ON p1.person_id=p2.person_id;

SELECT DISTINCT p1.first_name
FROM persons AS p1
CROSS JOIN likes AS p2
ON p1.person_id=p2.person_id
WHERE p2.food!='Beer';


SELECT DISTINCT p1.first_name
FROM persons AS p1
JOIN likes AS p2
ON p1.person_id=p2.person_id
GROUP BY food HAVING COUNT(*)>2;

SELECT DISTINCT first_name
FROM persons AS p1
JOIN likes AS p2
ON p1.person_id=p2.person_id
GROUP BY food 







