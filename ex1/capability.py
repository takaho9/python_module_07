from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal() -> None:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform() -> None:
        pass

    @abstractmethod
    def revert() -> None:
        pass

