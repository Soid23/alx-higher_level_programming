-- displays the average temperature in a descending order.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temparatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
