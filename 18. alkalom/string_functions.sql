/*
 * String függvények és string műveletek
 * 
 * */


select * from employees_hr eh ;
select * from countries_hr ch ;
select * from departments_hr dh ;
select * from dependents_hr dh ;
select * from jobs_hr jh ;
select * from locations_hr lh ;
select * from regions_hr rh ;

/* concatenation */
select
eh.first_name || ' ' || eh.last_name, -- concatenate with pipe operator
concat(eh.first_name, ' ', eh.last_name) -- concat function
from employees_hr eh 
;

select * from employees_hr;


select ASCII('A'), CHR(65);

/*
 * position - a keresett string hanyadik karakter
 * substring - a vizsgált stringból egy sub stringet kivesz a megadott pozícióból
 * replace - egy stringet lecserél egy másik stringben: minden előfordulását
 * 
 * 
 * */
select
position('@' in t.email),
substring(t.email, position('@' in t.email) + 1),
substring(t.email, position('@' in t.email) + 1, 5),
substring(t.email, 1, position('@' in t.email) - 1),
replace(t.email, '@', '//'),
replace(t.email, 'ee', 'É'),
t.email 
from employees_hr t;


select left('nem is tudom', 5),
substring('nem is tudom', 1, 5),
right('nem is tudom', 4),
rpad('w3r', 4, 'esource'),
rtrim('rtrimtest', 'best');
;

/*
 * cast - átalakít 1 típust egy megadott másik típussá, ha az lehetséges
 * */
select
cast(t.salary as text),
t.salary
from employees_hr t;

/*
 * coalesce - visszadja az első nem null értéket,
 * 			  a nullnak tudunk más értéket beállítani
 * */

select
t.manager_id,
coalesce(t.manager_id, 0),
from employees_hr t;

select avg(t.manager_id), avg(coalesce(t.manager_id, 0)) from employees_hr t;

select * from employees_hr t;

/*
 * case when - feltételek sql-ben
 * 
 * */

select
t.job_id,
-- switch case
case
	t.job_id
	when 4 then 'négyes'
	when 5 then 'ötös'
	else 'mindegy' end as test,
-- if else
case 
	when t.job_id = 4 then 'négys'
	when t.job_id = 5 then 'öts'
	else 'mindegy' end as test2,
from employees_hr t;


select
t.phone_number,
substring(t.phone_number, 5, 3),
substring(right(t.phone_number, 4), 2,1),
case 
	when substring(t.phone_number, 5, 3) = '123' then
		case 
			when substring(right(t.phone_number, 4), 2,1) = '5' then replace(t.phone_number, '123', '666')
			when substring(right(t.phone_number, 4), 1,1) = '3' then replace(t.phone_number, '123', '777')
			else t.phone_number 
		end		
		else t.phone_number
	end as ph_case
from employees_hr t;

--- csütörtökön térjünk erre vissza: Yettel max(case when-es feladat)
select * from employees_hr t
where t.manager_id is null 
or t.employee_id in (145, 178);
