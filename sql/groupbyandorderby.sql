SELECT occupation
FROM employee_salary
GROUP BY occupation
;

-- group by garda chai ki select garya item ra gorup by garya eutai huna parcha or aggrigate fucn use vako huna parcha
select occupation, salary
from employee_salary
group by occupation, salary;

select occupation, AVG(salary)
from employee_salary
group by occupation;


SELECT gender, MIN(age), MAX(age), COUNT(age),AVG(age)
FROM employee_demographics
GROUP BY gender
;


--orderby

select * 
from employee_demographics
order by age
--default ma acending ma huncha


select *
from employee_demographics
order by gender desc,age

SELECT *
FROM employee_demographics
ORDER BY 2 DESC, 4 ASC;
--col ko position bata ni garna milcha
