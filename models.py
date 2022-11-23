from dataclasses import dataclass
from typing import List


@dataclass
class Recipe:
    name: str
    category: str
    calories: float
    ingredients: List
    instructions: List

    def dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "calories": self.calories,
            "ingredients": self.ingredients,
            "instructions": self.instructions
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


@dataclass
class Instruction:
    definition: str
    index: int

    def dict(self):
        return {
            "definition": self.definition,
            "index": self.index
        }
