from .capability import HealCapability, TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        if self._transformed:
            return f"{self._name} cannot be transformed."
        else:
            self._transformed = True
            return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self._name} returns to normal."
        else:
            return f"{self._name} cannot be reverted."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        if self._transformed:
            return f"{self._name} cannot be transformed."
        else:
            self._transformed = True
            return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self._name} stabilizes its form."
        else:
            return f"{self._name} cannot be reverted."
