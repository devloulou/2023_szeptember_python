/*
 * dátum függvényt
 * 
 * */


select
-----------date--------------
eh.hire_date,
to_char(eh.hire_date, 'YYYYMMDD'),
to_char(now(), 'YYYYMMDD HH24:MI:SS MS'),
to_char(eh.hire_date, 'day'),
to_char(eh.hire_date, 'month'),
to_char(eh.hire_date, 'Q'),
-----------------------------
----------- numeric----------
eh.salary,
to_char(eh.salary, '0999G999G999D9 l')
from employees_hr eh ;

select extract(year from now()),
to_char(now(), 'YYYY'),
extract(month from now()),
extract(day from now()),
extract(hour from now()),
extract(minute from now()),
extract(second from now()),
date'2030-01-20' + interval '12 hour',
to_char(to_date('2023.10.12 10:34:23', 'YYYY.MM.DD HH24:MI:SS'), 'YYYY.MM.DD HH24:MI:SS'),
to_timestamp('2023.10.12 10:34:23', 'YYYY.MM.DD HH24:MI:SS')
;



