/*
 * join műveletek
 * 
 * 
 * Táblákat fogunk tudni összekötni
 * 
 * inner join
 * left outer join
 * right outer join
 * full outer join
 * cross join
 * 
 * */

select * from employees_hr eh ;
select * from countries_hr ch ;
select * from departments_hr dh ;
select * from dependents_hr dh ;
select * from jobs_hr jh ;
select * from locations_hr lh ;
select * from regions_hr rh ;

/* inner join*/
select jh.job_title, eh.* from employees_hr eh 
inner join jobs_hr jh on eh.job_id = jh.job_id ;

/*ilyet nem csinálunk*/
select jh.job_title, eh.* from employees_hr eh 
inner join jobs_hr jh on eh.job_id != jh.job_id ;



/* left join 
 * 
 * Melyik lokáció melyik régióhoz tartozik? - inner join
 * 
 * Mely országokban nincs lokáció még hozzárendelve?
 * */
select lh.*, ch.region_id, rh.region_name  from locations_hr lh
inner join countries_hr ch on lh.country_id = ch.country_id --and ch.country_id != 'US'
inner join regions_hr rh on ch.region_id = rh.region_id 

;
-----------------------------------------------------------------------

/*
 * Mely országokban nincs lokáció még hozzárendelve?
 * */
select * from regions_hr rh
left join countries_hr ch on rh.region_id = ch.region_id 
left join locations_hr lh on ch.country_id = lh.country_id 
where 1 = 1
--lh.location_id is null
--and lh.country_id != 'US'
--order by region_name
;


select * from locations_hr lh ;
-----------------------------------------------------------------------

/*
 * Right Join
 * */

select * from regions_hr rh
right join countries_hr ch on rh.region_id = ch.region_id 
right join locations_hr lh on ch.country_id = lh.country_id ;


select *  from locations_hr lh 
right join countries_hr ch on lh.country_id = ch.country_id 
right join regions_hr rh on ch.region_id = rh.region_id 
;


/*
 * Full join
 * 
 */
select * from regions_hr rh
full join countries_hr ch on rh.region_id = ch.region_id 
full join locations_hr lh on ch.country_id = lh.country_id ;

------------------------------
select * from regions_hr rh
inner join countries_hr ch on rh.region_id = ch.region_id 
left join locations_hr lh on ch.country_id = lh.country_id ;

select ch.country_name  from countries_hr ch
left join locations_hr lh on ch.country_id = lh.country_id 
where lh.location_id is null;

/*
 * 
 * Cross join
 * 
 * Descartes szorzat
 * 
 * (1, 2) - (3, 4, 5) -> 1-3, 1-4, 1-5, 2-3, 2-4, 2-5, 
 * 
 * */

select * from regions_hr,
locations_hr lh,
employees_hr eh,
information_schema.columns -- descartes szorzat
;

select * from regions_hr rh 
inner join locations_hr lh on true -- 1=1
;

select * from regions_hr rh 
cross join locations_hr lh ;


select * from information_schema.columns

create table perf_test as 
select * from regions_hr,
locations_hr lh,
employees_hr eh,
information_schema.columns;

update perf_test set manager_id = 200;
select * from perf_test;
