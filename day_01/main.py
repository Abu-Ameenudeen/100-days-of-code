print("Welcome to the Band Name Generator!")

city: str = input("What's the name of the city you grew up in? ").strip()
pet_name: str =  input("What's your pet's name? ").strip()

band_name: str = f"{city} {pet_name}".title()

print(f"Your band name could be: {band_name}")