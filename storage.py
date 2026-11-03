import json

def load_coffees():
    try:
        with open("coffees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Application stopped to protect existing data.")
        raise SystemExit(1)
    
def save_coffees(coffees):
    with open("coffees.json", "w") as file:
        json.dump(coffees, file, indent=4)