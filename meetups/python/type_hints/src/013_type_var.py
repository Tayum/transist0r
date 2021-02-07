from typing import Type, TypeVar


LiquidT = TypeVar("LiquidT", bound="Liquid")


class Liquid:
    def __init__(self, liters: int) -> None:
        self.liters = liters

    @property
    def is_alcoholic(self) -> bool:
        raise NotImplemented


class Water(Liquid):
    """Common Water"""

    @property
    def is_alcoholic(self) -> bool:
        return False


class Wine(Liquid):
    """Precious Wine"""

    def is_alcoholic(self) -> bool:
        return True

    @staticmethod
    def avg_alcohol() -> float:
        return 12.5


def transform(val: Liquid, to: Type[LiquidT]) -> LiquidT:
    return to(val.liters)


wine = transform(Water(100), Wine)
