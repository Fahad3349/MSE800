from abc import ABC, abstractmethod


class Fish(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def category(self):
        pass


class Goldfish(Fish):
    def category(self):
        return "Goldfish"


class Shark(Fish):
    def category(self):
        return "Shark"


class Angelfish(Fish):
    def category(self):
        return "Angelfish"


class Tuna(Fish):
    def category(self):
        return "Tuna"


class Salmon(Fish):
    def category(self):
        return "Salmon"


class FishFactory:
    @staticmethod
    def create_fish(fish_type, quantity):
        fish_type = fish_type.lower()

        if fish_type == "goldfish":
            return Goldfish(quantity)
        elif fish_type == "shark":
            return Shark(quantity)
        elif fish_type == "angelfish":
            return Angelfish(quantity)
        elif fish_type == "tuna":
            return Tuna(quantity)
        elif fish_type == "salmon":
            return Salmon(quantity)
        else:
            raise ValueError("Invalid fish category")