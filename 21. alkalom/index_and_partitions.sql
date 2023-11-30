/*
 * Index
 * Gyorsítja az adat elérést, az által,
 * hogy az adatot fizikailag nem
 * a táblában keresi, hanem az index struktúrában
 * megkeresi az adat helyét, és ha a helye megvan,
 * akkor megvan az adat is
 * 
 * Ha egy táblán nincs index, akkor a tábla adatai lekérdezésekor
 * a teljes táblát végig nézi a adatbázis motor -> full table scan
 * 
 * Amire figyelni kell:
 *  1. nem teszek minden mezőre indexet:
 * 		- minél több index van 1 táblán,
 * 			az insert és update meg a delete művelet annál lassab lesz
 * 
 * 	2. azokra a mezőkre érdemes indexet tenni:
 * 		- gyakran használod join-okhoz
 * 			- ha az indexált mezőn típus konverziót (pl. stringből dátum) és
 * 			 / vagy egyéb function műveletet használok, akkor elveszíthetem
 * 			 az index használat előnyét
 * 		- gyakran használod where feltételekben
 * 
 *  3. b-tree indexet nem érdemes olyan mezőre tenni, ahol kevés unique érték van -> sok az ismétlődő rekord
 * 
 * B-tree index típusa:
 *  - normal index
 *  - unique (pl. Primary key)
 * 
 * 
 * 2 típusról beszélünk (több típus létezik):
 * b-tree - b-fa index
 * bitmap index
 * 
 * Bitmap index:
 * 
 * 1. Akkor célszer használni
 * 	ahol kevés unique érték van -> sok az ismétlődő rekord
 * 
 * Explain plan-re rákereshettek
 * 
 * ---------------------------------------------------
 * Partíció 
 * 
 * Táblához tartozó optimalizciós megoldás
 * "Feldarabolod" a táblát, valamilyen logika szerint
 *  - Range Partitioning
 *  - List Partitioning
 *  - Hash Partitioning
 * 
 * Akkor érdemes partícionálnod, ha sok adatot, sokan akarnak használni
 * 
 * */

/* like */
select * from employees_hr eh 
where 
--eh.phone_number like '515%' -- az 515-el kezdődő telefonszámok
--eh.phone_number like '%569' -- 569 végű telefonszámok
--eh.phone_number like '%123%' -- azok a telefonszámok, amelyek tartalmazzák a 123-at
eh.first_name ilike 'da_i_%' -- _ 1 karaktert helyettesít
;

/*
 * Halmazműveletek
 * 
 * union és union all - egyesítés
 * union - a duplikációkat kiszűri
 * union all - mindent egyesítem, nem törődöm a duplikációval
 * */

select 'alma' as gy
union 
select 'barack' as gy
union all
select 'alma' as gy;


/*
 * Halmazművelet:
 * intersect - közös metszet
 * */
select 'alma' as gy
intersect 
select * from (
select 'barack' as gy
union
select 'alma' as gy) b
;

/*
 * Halmazmvelet
 * */

select 'alma' as gy
except 
select * from (
select 'barack' as gy
union
select 'alma' as gy) b;


select * from (
select 'barack' as gy
union
select 'alma' as gy) b
except
select 'alma' as gy;


explain select * from regions_hr rh
inner join countries_hr ch on rh.region_id = ch.region_id 
inner join locations_hr lh on ch.country_id = lh.country_id ;




--------------------
CREATE TABLE measurement (
    city_id         int not null,
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (logdate);


CREATE TABLE measurement_y2006m02 PARTITION OF measurement
    FOR VALUES FROM ('2006-02-01') TO ('2006-03-01');
    
CREATE TABLE measurement_y2006m03 PARTITION OF measurement
    FOR VALUES FROM ('2006-03-01') TO ('2006-04-01');
    
INSERT INTO public.measurement
(city_id, logdate, peaktemp, unitsales)
VALUES(0, date'2006-02-27', 0, 0);

INSERT INTO public.measurement
(city_id, logdate, peaktemp, unitsales)
VALUES(0, date'2006-03-27', 0, 0);

select * from measurement_y2006m02 t;

select * from measurement_y2006m03 t;
;


