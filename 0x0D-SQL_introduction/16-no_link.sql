--Lists all records when name not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
