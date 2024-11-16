"""
def city_country(city, country):
    return f"{city}, {country}"

locations = {
    'USA': 'Anytown',
    'Canada': 'Montreal',
    'Mexico': 'Mexico City',
}

for country, city in locations.items():
    print(city_country(city, country))
"""

"""
def albums(artist, album):
    dict.append({artist: album})

dict = []
albums_num = 0
while True:
    if albums_num < 3:
        artist = input("Artist: ")
        album = input("Album: ")
        albums(artist, album)
        albums_num += 1
    else:
        print(dict)
        break
"""


def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)

print(user_profile["field"])
