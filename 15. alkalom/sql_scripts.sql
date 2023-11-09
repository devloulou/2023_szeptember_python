/*
 * Adatbázis szerepe:
 * Struktúráltan tároljunk és elérhető tegyünk adatokat
 * amelyeket kedvünkre alakíthatunk anélkül, hogy megváltoztatnánk
 * az adatok valódi értékét
 * 
 * Logikailag értelmezhető módon
 * 
 * Tábla struktúra kialakításának menetét
 * adatmodellezésnek nevezzük
 * 
 * Megszorítások - constraintek
 * 
 * Not null - nem lehet null az értéke a mezőnek: az üres string != null értékkel
 * Check Constraints - valamilyen ellenőrzéshez / logikai vizsgálathoz köti azt, hogy 
 * az adat bekerülhet e a mezőbe
 * 
 * Unique - egyedi értéket kell tartalmaznia az adatbázisnak
 * 
 * Primary key - elsődleges kulcs: not null és unique
 * 		2 feladata van: - egyértelmű azonosítás
 * 						- csak primary key-el tudsz kapcsolatot kialakítani
 * 							2 vagy több tábla között
 * 
 * 	A kapcsolat: szülő - gyermek kapcsolat, 
 * 
 * Foreign  Key - idegen kulcs 
 * */

drop table my_test_table;

create table my_test_table (
	--id integer unique,
	id integer primary key,	
	name text not null,
	salary integer check (salary > 1000 and salary is not null)
);


create table foreing_key_test (
	id integer primary key,
	test_id integer references my_test_table(id),
	col1 text
);


select * from foreing_key_test;

insert into foreing_key_test (id, test_id, col1) 
values (1, 2, 'agsasg');

-- alter utasítás: meglévő objektumot tudok módosítani
alter table my_test_table
add column salary integer check (salary > 1000);


--- minden recordot kidob a táblából
truncate table my_test_table;
-- minden recordot töröl a táblából
delete from my_test_table where name = '';

insert into my_test_table (id, name, salary) values (1, 'Ricsi', 1001);
insert into my_test_table (id, name, salary) values (2, 'Ricsi', 1001);
insert into my_test_table (id, name, salary) values (3, '', 1001);


insert into my_test_table (id, name, salary) values (null, 'Ricsi', 1001);


-- direkt hibás insert
--insert into my_test_table (id, name) values (1, null);

select * from my_test_table t
--where name is null
where name = ''
;

