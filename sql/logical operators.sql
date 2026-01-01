
-- Logical operators
select * 
from employee_salary
where dept_id < 5 AND salary <30000;

select *
from employee_salary
where dept_id <= 1 OR salary < 30000;

select * 
from employee_salary
where  NOT dept_id = 1;

--between
select salary
from employee_salary
where salary between 40000 AND 55000;

--not between
select salary
from employee_salary
where salary not between 40000 AND 55000;


--in
select first_name,salary
from employee_salary
where  salary in (50000,75000)
order by salary;