from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability
from typing import cast


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this Normal strategy"
            )
        else:
            print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        else:
            transformer = cast(TransformCapability, creature)
            print(transformer.transform())
            print(creature.attack())
            print(transformer.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )
        else:
            defence = cast(HealCapability, creature)
            print(creature.attack())
            print(defence.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
