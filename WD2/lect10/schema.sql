DROP TABLE IF EXISTS wines;
 
CREATE TABLE wines
(
    wine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
);






INSERT INTO wines (name, price, description)
VALUES
  ('Dingo Dribble', 12.33, 'Goes well with a snake steak.'),
  ('Emu Emission', 17.99, 'A spunky wine for every occasion!'),
  ('Koala Kool-aid', 12.33, 'With a hint of eucalyptus.'),
  ('Platypus Pish', 15.99, 'A fizzy and frothy concoction.'),
  ('Roo Runoff', 8.99, 'Quite acidic.'),
  ('Wombat Waz', 10.99, 'The taste of the outback.');