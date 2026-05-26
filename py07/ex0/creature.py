from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_: str) -> None:
        self.name: str = name
        self.type: str = type_

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        ...
