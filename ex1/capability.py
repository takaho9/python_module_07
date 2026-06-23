from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal() -> str:
        pass
class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False

    @abstractmethod
    def transform() -> str:
        pass

    @abstractmethod
    def revert() -> str:
        pass
