"""
Dictionary - szótár 

my_dict = {} -> kulcs - érték párokat adok meg

kulcs:
    - mindig egyedi, nem lehet több ugyan olyan nevű kulcs 1 szinten
    - a kulcsnak hashalhető adattípusnak kell lennie:  int , float , str , tuple , None

A dictionary egy mutable data type -> megváltoztatható
    - lehet hozzáadni kulcs-érték párokat
    - lehet törölni kulcs - érték párokat
    - lehet módosítani kulcs - érték párokat
  
Iterable object 
"""

my_dict = {
    "color": "black",
    "brand": "BMW",
    "price": 100_000,
    0: 123,
    "color": "red"
}

# print(my_dict["brand"])
# print(my_dict["color"])
# print(my_dict[0])

############################################
# új kulcs - érték hozzáadása

my_dict["shop"] = "Budapest"
my_dict.update({"motor_type": "benzin", "name": "Erik"})

# meglévő kulcs - érték módosítása
my_dict = {
    "color": "black",
    "brand": "BMW",
    "price": 100_000
}

my_dict['color'] = "red"
my_dict.update({"brand": "Mercedes", "price": 200_000})

# print(my_dict)
########################################################################
# kulcs - érték pár törlése

my_dict = {
    "color": "black",
    "brand": "BMW",
    "price": 100_000
}

# my_dict.clear() - minden kulcs - érték pár törlése
my_dict.pop('color')
# my_dict.pop("name")

my_dict.popitem() # az utoljára berakott kulcs - érték párt dobja el

del my_dict['brand']

# print(my_dict)
##########################################################################################
# layers of dictionary

my_dict = {
    "subjects": {
        "irodalom":{
            "tanar": "Kati néni",
            "orak": ["hetfő", "kedd"]
        },
        "matek": { 
            "tanar": "Béla bá",
            "orak": ["kedd", "szerda"]
        },
        "tesi": {
            "tanar": "Jocó bá",
            "orak": ["hetfő", "péntek"]
        }
    }
}


# print(my_dict['subjects']['irodalom']['orak'][1])
# print(my_dict['subjects']['matek']['orak'][1])




# életszerű példát:
my_dict2 = {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    },
                    {
                        "name":"asprin",
                        "dose":"",
                        "strength":"250 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}


print(my_dict2['problems'][0]['Diabetes'][0]\
      ['medications'][0]['medicationsClasses'][0]['className'][0]['associatedDrug'][0]['strength'])

print(my_dict2.keys())
print(my_dict2.values())
