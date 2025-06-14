import json


travel_log = [
    {
        "country": "Franch",
        "visits ": 12,
        "cities": ["paris", "lillie", "dijon"]
    },
    {
        "country": "Bangladesh",
        "visits": 50,
        "cities": ["dhaka", "Barishal", "ctg", "shylet", "khulna"]
    },

]


def add_new_country(country_name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("russia", 2, ["moscow", "st petursburg"])
print(json.dumps(travel_log, indent=4))
