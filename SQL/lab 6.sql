SELECT *
FROM movies;

/*SELECT COUNT(title)
FROM movies;

SELECT COUNT(title)
FROM movies
WHERE yr='1975';*/


/*SELECT *
FROM actors
WHERE name='Clint Eastwood';*/

/*SELECT *
FROM castings;

SELECT *
FROM actors;*/

---SELECT *
---FROM castings as c JOIN actors as a
---ON c.actorid=a.id;

/*SELECT *
FROM castings as c JOIN actors as a
ON c.actorid=a.id
WHERE a.name='Clint Eastwood';

SELECT DISTINCT movieid
FROM castings as c JOIN actors as a
ON c.actorid=a.id
WHERE a.name='Clint Eastwood';

SELECT DISTINCT m.title, m.yr
FROM movies as m
    JOIN castings as c
    JOIN actors as a
ON 
c.movieid=m.id
and c.actorid=a.id
WHERE a.name='Clint Eastwood'
ORDER BY m.yr ASC;*/

/*SELECT DISTINCT a.name
FROM movies as m
    JOIN castings as c
    JOIN actors as a
ON 
c.movieid=m.id
and c.actorid=a.id
WHERE m.title='Citizen Kane'
ORDER BY m.yr ASC;*/

/*SELECT DISTINCT a.name
FROM movies as m
    JOIN castings as c
    JOIN actors as a
ON 
c.movieid=m.id
and c.actorid=a.id
WHERE m.title='Vertigo'
OR m.title='Rear Window';*/

/*SELECT DISTINCT m.title
FROM movies as m
    JOIN castings as c
    JOIN actors as a
ON 
c.movieid=m.id
and c.actorid=a.id
WHERE m.director='28';

SELECT DISTINCT m2.title
FROM movies as m1
    JOIN movies as m2
ON 
m1.director=m2.director
WHERE m1.title='Godfather, The';*/

SELECT m1.title, m1.yr, m2.yr
FROM movies as m1
    JOIN movies as m2
ON 
m1.title=m2.title
WHERE m1.yr<>m2.yr;

SELECT title
FROM movies
WHERE title || 'II'
OR title || 'IV'
OR title || 'V';



/*SELECT *
FROM castings
WHERE actorid='2';*/




SELECT OffenceDate, Description, Drivers.LicenceNo, Surname, Forename
FROM Drivers 
JOIN Prosecutions 
ON D.LicenceNo = P.LicenceNo 
WHERE Prosecutions.OffenceDate LIKE '%-15'
GROUP BY LicenceNo
ORDER BY Surname Desc;