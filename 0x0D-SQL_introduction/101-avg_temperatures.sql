-- Import a file then compute it
-- SOURCE temperatures.sql;
SOURCE main_0.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
