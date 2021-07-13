-- find the average temperatures in each city and show them
SELECT city, avg(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
