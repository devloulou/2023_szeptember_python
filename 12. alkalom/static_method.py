"""
Staticmethods - statikus függvények
Akkor célszerű hhasználni, ha valamilyen utility megoldást fejlesztesz, 
amelyben NEM AKARSZ SEMMILYEN AZ OBJEKTUMHOZ TARTOZÓ ATTRIBUTUME-OT HASZNÁLNI

Statichmetod: - nem tudja használni az objektumhoz tartozó attribútumokat -> self-et
Ahhoz, hogy használjam, nem szükséges a példányosítás, egyszerűen az osztályon keresztül tudom használni

Minden ami self-el van ellátva, az egy instance attributum
"""

class FileHandler:

    def __init__(self):
        self.price = 10_000

    @staticmethod
    def get_data_from_txt(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()

        return data
    
    def hello(self):
        # self.get_data_from_txt()
        print("hello")


if __name__ == '__main__':
    file_path = r"C:\WORK\2023_szeptember_python\12. alkalom\data\A Tale of Two Cities.txt"
    file_path2 = r"C:\WORK\2023_szeptember_python\12. alkalom\data\masik_konyv.txt"

    test = FileHandler()
    data = test.get_data_from_txt(file_path)
    data2 = FileHandler.get_data_from_txt(file_path2)
    # FileHandler.hello(test)

    print(data[0:10])
    print(data2[0:10])