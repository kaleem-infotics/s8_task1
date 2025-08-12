-- db/init.sql
CREATE TABLE if not EXISTS student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO student (name) VALUES ('Ali'), ('Sara'), ('Ahmed')
ON CONFLICT DO NOTHING;

-- Show the table contents
SELECT * FROM student;
