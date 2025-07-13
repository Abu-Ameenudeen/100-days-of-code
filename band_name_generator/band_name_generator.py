class BandNameGenerator:
    def __init__(self):
        self.pet_name = ""
        self.city = ""
    
    def get_user_input(self):
        self.city = input("What's the name of the city you grew up in? ").strip()
        self.pet_name = input("What's your pet's name? ").strip()
        
    def generate_name(self):
        return f"{self.city} {self.pet_name}".title()

    def run(self):
        print("Welcome to the Band Name Generator!")
        self.get_user_input()
        print(f"Your band name could be: {self.generate_name}")