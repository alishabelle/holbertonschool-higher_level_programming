-- top 3 city temp decending order
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR MONTH = 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
