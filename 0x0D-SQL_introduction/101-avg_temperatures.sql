-- find the average temps in each city and display  in order
SELECT city, avg(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
