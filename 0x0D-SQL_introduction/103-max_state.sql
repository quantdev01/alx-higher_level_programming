-- Temperature by max state
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state ASC;
