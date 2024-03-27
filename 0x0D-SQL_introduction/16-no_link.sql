-- Lists all records with the name value as name and score in descending order

SELECT score,
	name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
