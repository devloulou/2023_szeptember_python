select * from information_schema.columns t
where --t.table_name = 'jobs_hr'
t.column_name like '%job%';

select *from jobs_hr jh ;

select *from employees_hr eh 

/*
 * Feladatok:
 * 
 * Írj egy olyan sql lekérdezéseket,
 * amelyek választ adnak a következő kérdésekre:
 * 
 * 1. Ki keresi a legtöbbet és ki keresi a legkevesebbet a dolgozók közül?
 * 2. Melyik departmentben dolgozik a legötbb és legkevesebb ember?
 *  Ha 1 ember dolgozik, azt nem számítom a legkevesebbe.
 * 
 * 3. feladat: Mely régióban dolgozik a legtöbb alkalmazott?
 * Melyik ez a régió? Ez lehet 2 külön sql
 * 
 * 4. Ha adnék 10% fizetés emelést mindenkinek, akkor kinek lépné át a fizetése a maximum megadott 
 * értéket: Ha nincs ilyen, akkor ugyan ezt 30%-os emeléssel nézzétek meg
 * 
 * 5. Melyik vezetőnek hány alkalmazottja van?
 * 	  Melyik vezetőnek melyik alkalmazottja keres legtöbbet?
 * 	  Melyik vezető költi a legtöbbet a bérekre és mennyit?
 *	  Departmentenként melyik vezető mennyit költ bérekre?
 * */