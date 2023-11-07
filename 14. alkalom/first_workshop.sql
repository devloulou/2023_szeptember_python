/*
 * SQL modul
 *
 * PostgreSQL - RDBMS - Relational Database Management System
 * 
 * Relációs adatbázis
 * (NoSQL adatbázisok, gráf adatbázisok)
 * 
 * SQL - lekérdező nyelv , Structured Query Language
 * 
 * 2 fajta relációs adatbázis megközelítés van:
 * 	- OLTP - Online Transactional Processing - A kurzusin mi ezt fogjuk átvenni
 * 	- OLAP - Online Analitical Processing: 
 * 			DATA SCIENTISTEK, DATA ANALYSTOK, RIPORTING,
 * 			Data Engineerek -> BI - Business Intelligence
 *
 * OLTP felhasználási területe: pl. Netbank alkalmazás,
 * 								webshop
 * 
 * OLAP - Adattárház - DWH - Data Warehouse: elemezni akarod az adatokat
 * 											 a céges adatvagyon gazdálkodást
 * 											 különböző döntéshozatal támogatási funkciókat akarsz
 *
 * NoSQL adatbázis: nem SQL alapú -> nem relációs adatbázis
 * documentum és vvagy file alapú adattárolást valósítanak meg
 *
 * 
 * SQL nyelv:
 * 
 * DDL - Data Definition Language - amikor adatbázis objektumot akarok létrehozni
 * create, drop, alter, truncate, *comment, rename
 * 
 * DML - Data Manipulation Language - amikor az adatot akarom létrehozni / módosítani / törölni és vagy az objectumot akarom használni etc.
 * insert, update, delete, *lock, *call, #explain plan
 * 
 * DCL - Data Control Language - jobosultság kezeléshez szükséges utasítások
 * grant, revoke, roles
 * 
 * DQL - Data Query Language - az adatok lekérdezése
 * select
 *
 *  TCL - Transaction Control Language
 * commit, rollback
 * */

/*
 * Reláció: táblákba szervezem az adataimat
 * 			és a táblák között valamilyen kapcsolatot alakítok ki
 * 
 * 
 * MINDEN SQL UTASÍTÁS UTÁN TEGYETEK PONTOSVESSZŐT ;
 * */


create table my_first_table(
	my_id integer,
	description text -- szöveges adattípus
);

-- insert utasítás - adatot tölt be a táblába
insert into my_first_table (my_id, description) values
(1, 'Ez egy leírás'); 

insert into my_first_table (my_id, description) values
(2, 'Ez egy másik leírás'); 

rollback;

commit;
-- * -  minden mező
select * from my_first_table;

select * from my_firts_table t
where t.my_id = 1;

update my_first_table set money = new_value
where id = "az én idm";


drop table my_first_table;

/*
 * 
 * Session: az adatbázishoz nyitott kapcsolat, ahol
 * az SQL utasításokat tudod lefuttatni
 * 
 * élő - idle (tétlen) - closed session
 * 
 * Minden utasítás a session-ön belül történik és csak akkor lép életbe globálisan
 * ha a session-ben kiadott utasítást valamilyen módon lezárom
 * 
 * 
 * Tranzakció kezelés:
 * 2 féle tranzakció kezelési metodika van:
 * 	- jóváhagyom a tranzakciót
 *  - megszíkítom / visszavonom a tranzakciót
 * 
 *  jóváhagyás - commit
 *  visszavonás - rollback
 * 
 * a le nem zárt tranzakció
 * blokkolhatja az adott objektum használatát: lock
 *  - sorszintű lock
 *  - tábla szintű lock
 * 
 * a session önáálló, egymástól független életet él, csak a lezárt tranzakció
 * után lesz a változás
 * globálisan elérhető az adatbázisban
 * */




