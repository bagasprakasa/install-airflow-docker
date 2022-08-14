CREATE TABLE IF NOT EXISTS sales (
    id INT PRIMARY KEY,
    creation_date DATE NOT NULL,
    sale_value INT);

INSERT INTO 
    sales (id, creation_date,sale_value)
VALUES 
    (0, '2021-12-12', 1000),
    (1, '2021-12-13', 2000);