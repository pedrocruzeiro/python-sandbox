travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(name, visits, cities):
    # First approach
    # country_dict = {
    #     "country": name,
    #     "visits": visits,
    #     "cities": cities,
    # }
    # Other possibility

    country_dict = {}
    country_dict["country"] = name
    country_dict["visits"] = visits
    country_dict["cities"] = cities

    travel_log.append(country_dict)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
