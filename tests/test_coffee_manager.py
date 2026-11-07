import coffee_manager

def test_find_coffee_by_name_existing():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil"},
        {"name": "Aquia", "origin": "Costa Rica"},
        {"name": "Huila", "origin": "Colombia"}
    ]

    # Act
    result = coffee_manager.find_coffee_by_name(coffees, "Mina")

    # Assert
    assert result == {"name": "Mina", "origin": "Brazil"}

def test_find_coffee_by_name_missing():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil"},
        {"name": "Aquia", "origin": "Costa Rica"},
        {"name": "Huila", "origin": "Colombia"}
    ]

    # Act
    result = coffee_manager.find_coffee_by_name(coffees, "Yamaniya")

    # Assert
    assert result is None


def test_find_coffee_by_name_case_insensitive():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil"},
        {"name": "Aquia", "origin": "Costa Rica"},
        {"name": "Huila", "origin": "Colombia"}
    ]

    # Act
    result = coffee_manager.find_coffee_by_name(coffees, "MINA")

    # Assert
    assert result == {"name": "Mina", "origin": "Brazil"}


def test_search_coffees_by_name():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil", "process": "Natural", "roast": "Medium"},
        {"name": "Aquia", "origin": "Costa Rica", "process": "Washed", "roast": "Light"}
    ]

    # Act
    result = coffee_manager.search_coffees(coffees, "min")

    # Assert
    assert result == [coffees[0]]


def test_search_coffees_by_origin():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil", "process": "Natural", "roast": "Medium"},
        {"name": "Aquia", "origin": "Costa Rica", "process": "Washed", "roast": "Light"}
    ]

    # Act
    result = coffee_manager.search_coffees(coffees, "COSTA")

    # Assert
    assert result == [coffees[1]]


def test_search_coffees_no_matches():
    # Arrange
    coffees = [
        {"name": "Mina", "origin": "Brazil", "process": "Natural", "roast": "Medium"}
    ]

    # Act
    result = coffee_manager.search_coffees(coffees, "Kenya")

    # Assert
    assert result == []


def test_get_new_coffee_details(monkeypatch):
    # Arrange
    coffees = []

    answers = iter([
        "Mina",
        "Brazil",
        "Natural",
        "Medium"
    ])

    monkeypatch.setattr(
        "ui.get_non_empty_input",
        lambda prompt: next(answers)
    )

    # Act
    result = coffee_manager.get_new_coffee_details(coffees)

    # Assert
    assert result == {
        "name": "Mina",
        "origin": "Brazil",
        "process": "Natural",
        "roast": "Medium"
    }