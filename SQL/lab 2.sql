CREATE TABLE planets
(
    name CHAR(10),
    diameter REAL,
    mass REAL,
    distance_from_the_sun REAL,
    number_of_moons INT
);

INSERT INTO planets 
(name, diameter, mass, distance_from_the_sun, number_of_moons)
VALUES 
('Mercury', '4,879KM', '330,104,000,000,000KG', '57.91MIL KM', '0'),
('Venus', '12,104KM', '4,867,320,000,000,000KG', '108.2MIL KM', '0'),
('Earth', '12,756KM', '5,972,190,000,000,000KG', '147 million km', '1'),
('Mars', '6,805KM', '641,693,000,000,000KG', '227.9 million km', '2'),
('Jupiter', '142,984KM', '1,898,130,000,000,000,000KG', ('4.9 AU' + '5.4 AU')/2, '67'),
('Saturn', '120,536KM', '568,319,000,000,000,000KG', '9.6 AU', '62'),
('Sqlonia', '1,184KM', '6.525,000,000,000', '79AU', 'Unknown');


INSERT INTO planets 
(name, mass)
VALUES 
('Uranus', '86,810,300,000,000,000KG'),
('Neptune', '102,410,000,000,000,000KG'),
('Pluto', '13,050,000,000,000KG');


UPDATE planets
SET
diameter='51,118 km', distance_from_the_sun='19.2 AU', number_of_moons='27'
WHERE name='Uranus';

UPDATE planets
SET
diameter='49,528 km', distance_from_the_sun='30 AU', number_of_moons='14'
WHERE name='Neptune';

UPDATE planets
SET
diameter='2,368 km', distance_from_the_sun='39.5 AU', number_of_moons='5'
WHERE name='Pluto';

DELETE FROM planets 
WHERE name='Sqlonia';

SELECT *
FROM planets;