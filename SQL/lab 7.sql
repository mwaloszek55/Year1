SELECT *
FROM movies;


SELECT *
FROM actors;


SELECT *
FROM castings;



/*SELECT id
FROM actors
WHERE id IN
    (SELECT actorid
    FROM castings
    WHERE movieid=
        (SELECT id
        FROM movies
        WHERE title='Big Sleep, The')
    );



SELECT title
FROM movies
WHERE director IN
    (SELECT director
    FROM movies
    WHERE title='Citizen Kane')
ORDER BY yr;


SELECT name
FROM actors
WHERE id IN
    (SELECT actorid
    FROM castings
    WHERE movieid=
        (SELECT id
        FROM movies
        WHERE title='Big Sleep, The')
    );
*/

/*SELECT id, title, yr
FROM movies
WHERE yr BETWEEN '1950' AND '1959'
UNION
SELECT id, title, yr
FROM movies
WHERE id IN
    (SELECT movieid
    FROM castings
    WHERE actorid IN
        (SELECT id
        FROM actors
        WHERE name='Elizabeth Taylor')
    )
ORDER BY yr;


SELECT title, score
FROM movies
WHERE score=
    (SELECT max(score)
    FROM movies);



SELECT id
FROM actors
WHERE id IN
    (SELECT actorid
    FROM castings
    GROUP BY movieid
    HAVING COUNT(*)>=10);



SELECT name
FROM actors
WHERE id IN
    (SELECT actorid
    FROM castings
    GROUP BY movieid
    HAVING COUNT(*)>=10);


SELECT title, score
FROM movies
WHERE score >= - 1 + (SELECT max(score) FROM movies);


SELECT name
FROM actors
WHERE id IN
    (SELECT actorid
    FROM castings
    WHERE movieid=
        (SELECT id
        FROM movies
        WHERE score >= 3)
    );


SELECT title, score
FROM movies
WHERE score=
    (SELECT max(score)
    FROM movies)
UNION
SELECT title, score
FROM movies
WHERE score=
    (SELECT min(score)
    FROM movies)
ORDER BY score DESC; 





--Question 11
SELECT title, yr
FROM movies
WHERE yr>
    (SELECT min(yr)
    FROM movies
    WHERE director=
        (SELECT director
        FROM movies
        WHERE title='Citizen Kane')
    )
INTERSECT
SELECT title, yr
FROM movies
WHERE director=
    (SELECT director
    FROM movies
    WHERE title='Citizen Kane');







SELECT title, yr
FROM movies
WHERE yr<
    (SELECT min(yr)
    FROM movies
    WHERE director=
        (SELECT director
        FROM movies
        WHERE title='Citizen Kane')
    )
INTERSECT
SELECT title, yr
FROM movies
WHERE director=
    (SELECT director
    FROM movies
    WHERE title='Citizen Kane');


SELECT title, score
FROM movies
WHERE score=
    (SELECT max(score)
    FROM movies
    WHERE yr BETWEEN 1940 AND 1949);



SELECT COUNT(*) as result
FROM castings
GROUP BY movieid
HAVING COUNT(*)
ORDER BY result desc
limit 1;

--Question 15 unfinished
SELECT director
FROM movies
GROUP BY id
HAVING COUNT(*)=
    (SELECT COUNT(*) as result
    FROM castings
    GROUP BY movieid
    HAVING COUNT(*)
    ORDER BY result desc
    limit 1);*/



--Question 17
SELECT title
FROM movies
WHERE director IN
    (SELECT director
    FROM movies
    WHERE title='Bananas')
INTERSECT
SELECT title
FROM movies
WHERE id IN
    (SELECT movieid
    FROM castings
    WHERE actorid=
        (SELECT id
        FROM actors
        WHERE name='Diane Keaton')
    );
