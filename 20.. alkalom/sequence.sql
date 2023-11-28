/*
 * sequence - szekvencia
 * 
 * Adatbázis objektum - create, drop, alter
 *  
 * (1, 2, 3, 4, 5, 6, 7, 8, 9 ......) - ez egy szekvencia
 * 
 * Felhasználás módja:
 * elsődleges kulcs generálásához
 * 
 * Ha nincs megadva, hogy owned - akkor insert során neked meg kell hívnod
 * a nextval('seq_name')
 * 
 * 1 sequencia 1 táblát töltsön
 * 
 * no cache - ha nem cache-lek el értéket előre, akkor az megadhatja
 * a rekordok valós sorrendjét is
 * főleg elosztott adatbázisok esetében lehet hasznos
 * 
 * owned by - hozzá rendeled a sequenciát 1 tábla 1 mezőjéhez
 * annak a mezőnek nem kell az insert során értéket adnod, mert automatikusan meghívja
 * a háttérben a sequencia next értékét
 * 
 * */
drop sequence my_test_seq;

create sequence my_test_seq
start with 1
increment by 1
cache 5;

select nextval('my_test_seq') ;

select nextval('my_test_seq');

create table my_seq_test (id integer);

truncate table my_seq_test;

insert into my_seq_test
select nextval('my_test_seq');

select * from my_seq_test;

create table my_serial_test (id serial);

insert into my_serial_test 
select;

select * from my_serial_test;

select now(), current_date
