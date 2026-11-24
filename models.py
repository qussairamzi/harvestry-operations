class Coffee:
    def __init__(self, name, origin, process, roast_level):
        self.name = name
        self.origin = origin
        self.process = process
        self.change_roast(roast_level)
    def describe(self):
        return f"{self.name} is a {self.roast_level} roast {self.process} coffee from {self.origin}."
    def change_roast(self, new_roast):
        valid_roasts = ["Light", "Medium", "Dark"]
        if new_roast not in valid_roasts:
            raise ValueError(f"Invalid roast level.")
        self.roast_level = new_roast
    def to_dict(self):
        return {
            "name": self.name,
            "origin": self.origin,
            "process": self.process,
            "roast": self.roast_level
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["origin"],
            data["process"],
            data["roast"]
    )

coffee_data = {
    "name": "Aquia",
    "origin": "Costa Rica",
    "process": "Washed",
    "roast": "Light"
}

aquia = Coffee.from_dict(coffee_data)

print(aquia.describe())
print(type(aquia))