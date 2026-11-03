from typing import Any

from pytest import MonkeyPatch
import pytest

import storage

import json

def test_load_coffees_missing_file(tmp_path: Any, monkeypatch: MonkeyPatch):
    # Arrange
    monkeypatch.chdir(tmp_path)

    # Act
    result = storage.load_coffees()

    # Assert
    assert result == []

def test_load_coffees_valid_json(tmp_path, monkeypatch):
    # Arrange
    test_coffees = [
        {
            "name": "Mina",
            "origin": "Brazil",
            "process": "Natural",
            "roast": "Medium"
        }
    ]

    test_file = tmp_path / "coffees.json"
    test_file.write_text(json.dumps(test_coffees))

    # Act
    monkeypatch.chdir(tmp_path)
    result = storage.load_coffees()

    # Assert
    assert result == test_coffees

def test_load_coffees_corrupted_json(tmp_path, monkeypatch):
    # Arrange
    test_file = tmp_path / "coffees.json"
    test_file.write_text("{invalid_json}")
    monkeypatch.chdir(tmp_path)

    # Act and Assert
    with pytest.raises(SystemExit):
        storage.load_coffees()

    # Assert data integrity
    assert test_file.read_text() == "{invalid_json}"

def test_save_coffees(tmp_path, monkeypatch):
    # Arrange
    test_coffees = [
        {
            "name": "Aquia",
            "origin": "Costa Rica",
            "process": "Washed",
            "roast": "Medium"
        }
    ]

    monkeypatch.chdir(tmp_path)

    # Act
    storage.save_coffees(test_coffees)

    # Assert
    test_file = tmp_path / "coffees.json"
    assert test_file.exists()

    saved_coffees = json.loads(test_file.read_text())
    assert saved_coffees == test_coffees