DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);



DROP TABLE IF EXISTS bikes;

CREATE TABLE bikes
(
    bike_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price VARCHAR(255) NOT NULL,
    descr TEXT,
    img BLOB
);

INSERT INTO bikes (name, price, descr, img)
VALUES ('Mongoose Title Elite Pro BMX Race Bike', '500 EURO', '“For high performance, stiff frame, well-made construction, lightweight, simple assembly, great geometry.”', '/~mw17/cgi-bin/ca1/run.py/static/mongoosetitle.jpg'),
       ('Mongoose L500 Freestyle BMX Bike', '300 EURO', '“Super strong, ultra-durable, lightweight, freestyles, clean & reliable drivetrain, easy to assemble.”', '/~mw17/cgi-bin/ca1/run.py/static/mongoosetitle.jpg'),
       ('Mongoose L80 Freestyle BMX Bike', '450 EURO', '“Sturdy and solid frame, reliable terrains, flexible and tough handlebars, strong control of brakes, lightweight, riding well at any terrains.”', '/~mw17/cgi-bin/ca1/run.py/static/mongoosetitle.jpg');






DROP TABLE IF EXISTS cart;

CREATE TABLE cart
(   
    user TEXT,
    item INT,
    quant INT
);



SELECT *
FROM cart;


