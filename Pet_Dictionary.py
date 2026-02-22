pet1 = {
    "animal": "Lizard",
    "owner": "Lizzy"
}

pet2 = {
    "animal": "Turtle",
    "owner": "Turner"
}

pet3 = {
    "animal": "Fish",
    "owner": "Finnly"
}

pet4 = {
    "animal": "Salamander",
    "owner": "Sally"
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print("Pet Information:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()