-- LIMIT and ALIASING

-- Limit is just going to specify how many rows you want in the output


SELECT *
FROM employee_demographics
LIMIT 3;

SELECT *
FROM employee_demographics
ORDER BY first_name
LIMIT 2 OFFSET 3;

-- this now says start at position 3 and take 2 rows after that
-- this is not used a lot in my opinion POSTGRES MA CHAI  OFFSET USE GARNA PARCHA MYSQL MA SIMPLE limit 2,3 garda huncha



-- ALIASING

-- aliasing is just a way to change the name of the column (for the most part)
-- it can also be used in joins, but we will look at that in the intermediate series
-- we can use the keyword AS to specify we are using an Alias
SELECT gender, AVG(age) AS Avg_age
FROM employee_demographics
GROUP BY gender
;

