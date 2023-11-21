/*
 * subselect - subquery
 * 
 * with
 * 
 * */

select * from employees_hr eh ;
select * from countries_hr ch ;
select * from departments_hr dh ;
select * from dependents_hr dh ;
select * from jobs_hr jh ;
select * from locations_hr lh ;
select * from regions_hr rh ;


/*
 * 
 * */

with base_data as (
select
	eh.employee_id,
	eh.first_name,
	eh.last_name,
	eh.email,
	eh.phone_number,
	eh.hire_date,
	jh.job_title,
	eh.salary,
	eh2.first_name || ' ' || eh2.last_name as manager,
	dh.department_name,
	jh.min_salary,
	jh.max_salary 
from
	employees_hr eh
inner join jobs_hr jh on
	eh.job_id = jh.job_id
inner join departments_hr dh on
	eh.department_id = dh.department_id
left join employees_hr eh2 on
	eh.manager_id = eh2.employee_id  
), agg as (
select
t.salary - t.min_salary as min_diff,
t.max_salary - t.salary as max_diff,
t.salary,
t.*
from base_data t
), min_agg as (
select min(min_diff) as min_diff, min(max_diff) as max_diff from agg
)
select * from agg t
where t.min_diff in (select min_diff from min_agg)
or t.max_diff in (select max_diff from min_agg)





