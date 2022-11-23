from dataclasses import dataclass
from typing import List


@dataclass
class Recipe:
    name: str
    category: str
    calories: float
    ingredients: List

    def dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "calories": self.calories,
            "ingredients": self.ingredients
        }


@dataclass
class Ingredients:
    string: str
    name: str
    amount: str
    unit: str

    def dict(self):
        return {
            "string": self.string,
            "name": self.name,
            "amount": self.amount,
            "unit": self.unit
        }
