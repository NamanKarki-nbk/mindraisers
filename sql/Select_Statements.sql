Select * 
from employee_salary
where salary = 50000
-- #we can use < > ! = also 

select * 
from employee_demographics
where gender != 'Male'

-- Like Statements
-- % vaneko anything that matches
SELECT *
FROM employee_demographics
where first_name LIKE 'L%';

-- __ vaneko chai specific value
select *
from employee_demographics
where first_name Like 'A___';

select *
from employee_demographics
where first_name Like 'A__%';

-- for case insenitive use ILIKE
