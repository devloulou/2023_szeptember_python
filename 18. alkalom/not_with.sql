
select
min(agg.min_diff) as min_diff,
min(agg.max_diff) as max_diff
from (
select
a.salary - a.min_salary as min_diff,
a.max_salary - a.salary as max_diff,
a.salary,
a.*
from (
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
	eh.manager_id = eh2.employee_id ) a
	) agg;
------------------------------------------------------	
select * from (select
a.salary - a.min_salary as min_diff,
a.max_salary - a.salary as max_diff,
a.salary,
a.*
from (
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
	eh.manager_id = eh2.employee_id ) a) d
where d.min_diff in (select
min(agg.min_diff) as min_diff
from (
select
a.salary - a.min_salary as min_diff,
a.max_salary - a.salary as max_diff,
a.salary,
a.*
from (
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
	eh.manager_id = eh2.employee_id ) a
	) agg)
or d.max_diff in (select
min(agg.max_diff) as max_diff
from (
select
a.salary - a.min_salary as min_diff,
a.max_salary - a.salary as max_diff,
a.salary,
a.*
from (
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
	eh.manager_id = eh2.employee_id ) a
	) agg)
