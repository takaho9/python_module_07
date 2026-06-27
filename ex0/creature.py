from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self._type = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self._type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
