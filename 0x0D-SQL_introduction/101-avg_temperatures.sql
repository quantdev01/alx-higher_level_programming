-- Import a file then compute it
SOURCE temperatures.sql;
SELECT city, AVG(value) as avg_temp from temperatures GROUP BY city ORDER BY avg_temp DESC;
