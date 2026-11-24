from models import Coffee
import pytest

def test_coffee_creation():
    coffee = Coffee("Mina", "Brazil", "Natural", "Medium")

    assert coffee.name == "Mina"
    assert coffee.origin == "Brazil"
    assert coffee.process == "Natural"
    assert coffee.roast_level == "Medium"

def test_coffee_to_dict():
    coffee = Coffee("Mina", "Brazil", "Natural", "Medium")
    coffee_dict = coffee.to_dict()

    assert coffee_dict["name"] == "Mina"
    assert coffee_dict["origin"] == "Brazil"
    assert coffee_dict["process"] == "Natural"
    assert coffee_dict["roast"] == "Medium"

def test_coffee_from_dict():
    coffee_data = {
        "name": "Mina",
        "origin": "Brazil",
        "process": "Natural",
        "roast": "Medium"
    }
    coffee = Coffee.from_dict(coffee_data)

    assert coffee.name == "Mina"
    assert coffee.origin == "Brazil"
    assert coffee.process == "Natural"
    assert coffee.roast_level == "Medium"

def test_invalid_roast():
    with pytest.raises(ValueError):
        Coffee("Mina", "Brazil", "Natural", "Banana")

def test_change_roast():
    coffee = Coffee("Mina", "Brazil", "Natural", "Medium")
    coffee.change_roast("Dark")

    assert coffee.roast_level == "Dark"

    with pytest.raises(ValueError):
        coffee.change_roast("Banana")

    assert coffee.roast_level == "Dark"