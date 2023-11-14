/*
 * Select utasítás
 * 
 *  "*" - minden oszlop a táblából
 * 
 *  alias - az alias azt teszi lehetővé, hogy egy megadott néven hivatkozzak
 * 	egy táblára vagy egy oszlopra
 * 
 * 	schema - 
 * 
 * */

select
employee_id,
--first_name as "kereszt név", -- ilyet ne csináljatok
first_name as kereszt_nev,
last_name,
salary,
eh.job_id
from public.employees_hr eh ;

-- filtering - filterezés - szűrés - 
-- where clause
-- and kapcsolat - or kapcsolat
select * from employees_hr eh 
where 
1 = 1
--and manager_id = 100 
and ((eh.employee_id < 110 and job_id = 5)
or eh.employee_id  = 110);


select * from employees_hr eh
where 1 = 1--eh.employee_id = 110 or eh.employee_id = 111 or eh.employee_id = 122
--eh.employee_id in (110, 111, 122)
and eh.employee_id not in (110, 111, 122);

/*
 * aggregáció - min, max, sum, avg, count
 * 
 * avg, count, min - a null értéket nem veszi figyelmbe!!!
 * 
 * */
select
min(eh.salary), -- minimum értéke az oszlopnak,
max(eh.salary), -- maximum értéke az oszlopnak
sum(eh.salary), -- összértéke az oszlopnak
avg(eh.salary), -- átlag értéke az oszlopnak
count(eh.salary) -- hány érték van az oszlopban
from employees_hr eh
where eh.employee_id < 120;


create table aggr_test (id serial, salary integer);

insert into aggr_test (id) values(1);

select sum(t.salary) from aggr_test t;

/*
 * Mutasd ki, hogy depmartmentenként mennyit költök az emberek
 * fizetésére
 * 
 * Group by - csoportokat hoz létre
 * */
 column "eh.department_id" must appear 
 in the GROUP BY clause or be used in an aggregate function

select sum(eh.salary),
avg(eh.salary),
min(eh.salary),
max(eh.salary),
count(eh.salary),
eh.department_id from employees_hr eh
where eh.department_id not in (4, 7, 1)
group by eh.department_id;

/* having */

select sum(eh.salary),
avg(eh.salary),
min(eh.salary),
max(eh.salary),
count(eh.salary),
eh.department_id from employees_hr eh
--where eh.department_id not in (4, 7, 1)
group by eh.department_id
having count(eh.salary) > 1;


/*
 * sorbarendezés
 * 
 * order by - ha van where és nincs group by, akkor a where után következik
 * 			- ha van group by és nincs having, akkor a group by után következik
 * 			- ha van having, akkor utána következik
 * 
 * order by mezo asc - növekvő sorrend, default növekvő
 * order by mezo desc - csökkenő sorrend
 * 
 * */



select sum(eh.salary) as sum_sal,
avg(eh.salary),
min(eh.salary),
max(eh.salary),
count(eh.salary),
eh.department_id from employees_hr eh
where eh.department_id not in (4, 7, 1)
group by eh.department_id
order by eh.department_id asc, sum_sal desc;



/* Top 4 legtöbbet költöt department */

select sum(eh.salary) as sum_sal,
avg(eh.salary),
min(eh.salary),
max(eh.salary),
count(eh.salary),
eh.department_id from employees_hr eh
where eh.department_id not in (4, 7, 1)
group by eh.department_id
order by sum_sal desc
limit 1;


/*
 * Analitikus függvények - window function
 * 
 * sum, min, max, avg, count
 * row_number,
 * rank,
 * dense_rank
 * lag
 * lead
 * 
 * 
 * function()over(partition by mezo order by mezo)
 * 	-- partition by opcionális
 *  -- order by is opcionális
 * 
 * */
select * from
(select
rank()over(partition by eh.department_id order by eh.salary desc) as rnk_salary,
dense_rank()over(partition by eh.department_id order by eh.salary desc) as dns_salary,
row_number()over(partition by eh.department_id order by eh.salary desc) as row_num_salary,
-- comulative sum: sum(eh.salary)over(partition by eh.department_id order by eh.salary desc) as sum_salary2,
min(eh.salary)over(partition by eh.department_id) as min_salary,
eh.first_name,
eh.last_name,
eh.salary,
eh.department_id 
from employees_hr as eh
--where eh.department_id = 9
--order by salary desc;
) base_data
where row_num_salary = 1




