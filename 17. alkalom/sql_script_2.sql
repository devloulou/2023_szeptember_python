/*
 * Subselect
 * 
 * Mely országokban nincs lokáció még hozzárendelve?
 * 
 * */
-- ez elég lassú tud lenni, érdemes kerülni

select count(*) from (
select * from perf_test t
where t.country_id is not null
limit 1000000) base_data;

select distinct t.country_id  from perf_test t
where t.country_id is not null
limit 1000000


select * from (
select ch.country_id,
ch.country_name,
(select distinct lh.country_id from locations_hr lh where ch.country_id = lh.country_id) as country_2
from countries_hr ch 
--where ch.country_id not in (select lh.country_id  from locations_hr lh);
) a
where a.country_2 is null
;

select * from countries_hr;