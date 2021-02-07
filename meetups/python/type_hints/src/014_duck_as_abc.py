from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self) -> str:
        pass


class DuffyDuck(Duck):
    def quack(self) -> str:
        return "<natural quack>"


class Human(Duck):
    def quack(self) -> str:
        return "<faked, yet quack>"


def call_quack(duck: Duck) -> None:
    print(duck.quack())


if __name__ == "__main__":
    call_quack(DuffyDuck())
    call_quack(Human())
