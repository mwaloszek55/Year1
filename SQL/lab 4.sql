SELECT *
FROM countries;

/*SELECT MAX(population)
FROM countries;



SELECT MAX(population)
FROM countries
WHERE region='Africa';


SELECT SUM(gdp)
FROM countries
WHERE region='Europe';


SELECT name, population
FROM countries
WHERE gdp IS NULL;


SELECT name, population
FROM countries
WHERE gdp IS NOT NULL;


SELECT name, region, AVG(gdp)
FROM countries
GROUP BY region;

SELECT *
FROM countries
WHERE name LIKE '%Africa%'
OR name LIKE '%Americas%'
OR name LIKE '%Asia-Pacific%'
OR name LIKE '%Europe%'
OR name LIKE '%Middle East%'
OR name LIKE '%North America%'
OR name LIKE '%South America%'
OR name LIKE '%South Asia%'; 


SELECT region, min(gdp), max(gdp)
FROM countries
GROUP BY region;   


SELECT region, count(name), sum(population)
FROM countries
GROUP BY region
HAVING region='Europe'
    OR region='Africa'
    OR region='Middle East';

SELECT sum(population), sum(area), sum(gdp)
FROM countries
WHERE name='France' OR name='Spain' OR name='Germany';


SELECT count(name)
FROM countries
WHERE population>'100000000'
ORDER BY region;

SELECT COUNT(*), MIN(name), MAX(name)
FROM countries 
GROUP BY SUBSTR(name, 1, 1);    */

SELECT name, region
FROM countries
ORDER BY region ASC, population DESC;


SELECT COUNT(*), sum(population)
FROM countries
WHERE population>'1000000000'
GROUP BY region;

SELECT c.name, t.name, t.population
FROM countries ASc 
JOIN cities AS t
ON c.code = t.countrycode
WHERE continent = ”Europe” AND c.capital = t.id;























