

my_dict = {} # dict

a = {1, 2, 3}  # set


planet_dict = {
    "Mercury" : 8,
    "Venus" : 6,
    "Earth": 5,
    "Mars" : 7,
    "Jupyter" : 1,
    "Saturn" : 2,
    "Uranus" : 3,
    "Neptune" : 4
    }

len(planet_dict)

planet_dict["Mars"] # 7
planet_dict["Jupyter"] # 1

planet_dict.get("Mars") # 7

planet_dict.get("Pluto") # there isn't, no error

planet_dict.get("Pluto", 0) # 0

print(planet_dict) #{'Mercury': 8, 'Venus': 6, 'Earth': 5, 'Mars': 7, 'Jupyter': 1, 'Saturn': 2, 'Uranus': 3, 'Neptune': 4}

planet_dict["Pluto"]  # KeyError: 'Pluto'



"Saturn" in planet_dict # True
"Pluto" in planet_dict  # False

planet_dict.keys()   # dict_keys(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupyter', 'Saturn', 'Uranus', 'Neptune'])
planet_dict.values() # dict_values([8, 6, 5, 7, 1, 2, 3, 4])


planet_dict["Pluto"] = 9
print(planet_dict)  # {'Mercury': 8, 'Venus': 6, 'Earth': 5, 'Mars': 7, 'Jupyter': 1, 'Saturn': 2, 'Uranus': 3, 'Neptune': 4, 'Pluto': 9}

planet_dict["Uranus"] = 4
planet_dict["Neptune"] = 3

print(planet_dict)  # {'Mercury': 8, 'Venus': 6, 'Earth': 5, 'Mars': 7, 'Jupyter': 1, 'Saturn': 2, 'Uranus': 4, 'Neptune': 3, 'Pluto': 9}


planet_dict.pop("Earth")
print(planet_dict)  # {'Mercury': 8, 'Venus': 6, 'Mars': 7, 'Jupyter': 1, 'Saturn': 2, 'Uranus': 4, 'Neptune': 3, 'Pluto': 9}




















