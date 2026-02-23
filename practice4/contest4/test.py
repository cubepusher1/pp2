import json 

people_string = '''

{
"people": [

    {
    "name": "Albert Einstein",
    "phone-number": "87777070121",
    "home-adress":  "jewland N12 house-3"
    },
    
    {
    "name": "Jeffrey Epstein",
    "phone_number": "86767676767",
    "home-adress": "an island in a sea"
    }
]
}

'''



data = json.loads(people_string)

for person in data["people"]:
    if person["name"] == "Albert Einstein":
        person["home-adress"] = "At the skies"
    else:
        person["home-adress"] = "Hell"

new_data = json.dumps(data, indent=2)

print(new_data)
print(people_string)