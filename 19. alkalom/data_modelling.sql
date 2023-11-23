/*
 * 
 * OLTP hogyan modellezünk adatot?
 * 
 * Mit nevezünk adat modellezésnek?
 * 
 * Normál forma
 * 
 * Normalization: megszűntetni a redundanciát, elkerülni az esetleges adat anomáliák kialakulását
 * az által, hogy kisebb táblákat hozok létre, amelyek között tábla szintű kapcsolat van
 * kialakítva
 * 
 * Ez a kapcsolat lehet:
 * 	- one to one: A táblában 1 rekordhoz B táblában csak 1 rekord kapcsolódhat
 *  - one to many: A táblában 1 rekordhoz B táblában több rekord kapcsolódhat
 *  - many to many: itt Bridge táblábával tudom ezt megoldani - Switch tábla - Kapcsoló táblának
 * 		- Van A táblám és B táblám, a kapcsoló táblában tárolom le azt, 
 * 			hogy A táblából mely rekordhoz mely rekordok kapcsolódnak a B Tábla rekordjai 
 * 
 * Adatmodellezés lépései:
 * 	- tételezzük fel, hogy már átbeszéltem az adat forrásával az adat típusát,
 * 	   az adatról tudok már annyit, hogy neki álljak a modellezésnek
 * 
 *  1. Conceptual Data model
 * ---------------------------------------
 * 	Employee			
	Employee ID - Pk			
			
	Deparments			
	Dep_id: primary key, Department_name			
			
	Jobs			
	Job_id, job_name, min_salary, max_salary		job_id: primary key	
 * ---------------------------------------
 *
 * 2. Logical Data Model - Logikai Adatmodell - Az adatmodell megtervezése, áábráázolása: kulcsok, kapcsolatok megjelenítése
 * 3. Phisical Ddata model - Fizikai adatmodell - Maga a Create utasítás
 * 
 * */

select * from employees_hr eh ;
select * from countries_hr ch ;
select * from departments_hr dh ;
select * from dependents_hr dh ;
select * from jobs_hr jh ;
select * from locations_hr lh ;
select * from regions_hr rh ;


select
eh.first_name,
eh.last_name,
eh.email,
eh.phone_number,
eh.hire_date,
jh.job_title,
eh.salary,
eh2.first_name  || ' ' || eh2.last_name as manager_name,
dh.department_name,
jh.min_salary,
jh.max_salary,
dh2.first_name || ' ' || dh2.last_name as family_member,
dh2.relationship as family_status,
lh.street_address || ' ' || lh.postal_code || ' ' || lh.city || ' ' || lh.state_province  as department_address,
ch.country_name as country_of_location,
rh.region_name as region_name
from employees_hr eh
inner join jobs_hr jh on eh.job_id = jh.job_id
left join employees_hr eh2 on eh.manager_id = eh2.employee_id
inner join departments_hr dh on eh.department_id = dh.department_id 
left join dependents_hr dh2 on eh.employee_id = dh2.employee_id
left join locations_hr lh on dh.location_id = lh.location_id
left join countries_hr ch on lh.country_id = ch.country_id 
left join regions_hr rh on ch.region_id = rh.region_id 

;


select * from dependents_hr dh 
inner join jobs_hr jh on dh.dependent_id = jh.job_id 


