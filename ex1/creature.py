from .capability import HealCapability, TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self._transformed:
            return f"{self.name} cannot be transformed."
        else:
            self._transformed = True
            return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self.name} returns to normal."
        else:
            return f"{self.name} cannot be reverted."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self._transformed:
            return f"{self.name} cannot be transformed."
        else:
            self._transformed = True
            return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self.name} stabilizes its form."
        else:
            return f"{self.name} cannot be reverted."
