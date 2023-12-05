"""
Data Engineering

Adatintegráció

Data Pipeline-okat fejleszt: 
    nyers adatot / denormalizált adatot eljuttatom egy  - 'általában' adatbázisba - integrált területre
    maga a pipeline az a kód és eszközök összessége, amit a fejlesztéshez használsz

Batch alapú feldolgozás:
    - ütemezett feldolgozás: napi vagy órás, vagy havi, vagy heti

Realtime adat integráció: (near realtime)
    - folyamatos adat integráció -> data streaming technológia 

----------------------------------------------
Az adat feldolgozásnak is van 2 kategóriája:
ETL vs ELT

ETL - Extract Transform Load
ELT - Extract Load Transform

Extract: a forrás adat kinyerése: file, adatbázis, etc. : amikor elhozod az integrálni kívánt adatot
Transform: 
    - adattisztítás: pl. hiányzó adatokkal mi történjen
                     pl. dátum megjelenítének egységesítése
                     az ismert / nem ismert adathibákkal mi történjen
    - adatmodellbe való integrálás:
        - egyedi kulcsok osztása
        - szülő - gyermek táblákba való rendezése az adatnak
Load: az adat végleges formájának a végleges helyére való integrálása: -> insert utasítás

""" 