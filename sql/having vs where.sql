-- Having vs Where

-- Both were created to filter rows of data, but they filter 2 separate things
-- Where is going to filters rows based off columns of data
-- Having is going to filter rows based off aggregated columns when grouped

SELECT occupation , AVG(salary)
FROM employee_salary
GROUP BY occupation
HAVING AVG(salary) > 40000;

-- SELECT occupation , AVG(salary) as avg_salary
-- FROM employee_salary
-- GROUP BY occupation
-- HAVING avg_salary > 40000;
-- col alias chai use garna mildaina postgres ma chai mysql jasari so


SELECT occupation, AVG(salary) AS avg_salary
FROM employee_salary
GROUP BY occupation
HAVING AVG(salary) > 40000;
