class Coffee:
    def __init__(self, name, origin, roast_level):
        self.name = name
        self.origin = origin
        self.change_roast(roast_level)
    def describe(self):
        return f"{self.name} is a {self.roast_level} roast coffee from {self.origin}."
    def change_roast(self, new_roast):
        valid_roasts = ["Light", "Medium", "Dark"]
        if new_roast not in valid_roasts:
            raise ValueError(f"Invalid roast level.")
        self.roast_level = new_roast
    
class DecafCoffee(Coffee):
    def describe(self):
        return f"{self.name} is a {self.roast_level} roast DECAFFEINATED coffee from {self.origin}."


decaf = DecafCoffee("Mina Decaf", "Brazil", "Medium")

print(decaf.describe())
