"""
Bolt kassza program

A boltnak vannak bizonnyos termékei
ezeket tudják a felhasználók megvenni

A kasszának a következőt kell tudnia lekezelni:

1. blokkot kell tudnunk visszaadni: tételesen a vásárolt termékeket
                                    nettó és bruttó ár                                    
Moduláris megközelítést szeretnék használni                                    
"""

"""
Mi a feladat?

Kell egy terméklista -> - "adatbázis", ahol a termékek ára szerepel
                        - mennnyiség

kassza működést kell megoldani:
    - blokkot kell adni a megadott leírás alapján
    - áfakulcs kiértékelődjön
    - összeeadni a tételeket
    - raktárkészletet csökkenteni: hibakezelés a standard esetekre: pl nincs elég termék
        szükség van egy készlet: termék és mennyiség -> dictionary pl.

Márk javaslata: keresés funkció házinak!    
"""

"""
Package felépítése:
    - modul 1: termékek
    - modul 2: maga a kassza működése
    - modul 3: raktárkészlet kezelést
"""

