from typing import Protocol


class QuackProtocol(Protocol):
    def quack(self) -> str:
        ...


class DuffyDuck:
    def quack(self) -> str:
        return "<natural quack>"


class Human:
    def quack(self) -> str:
        return "<faked, yet quack>"


def call_quack(quackable: QuackProtocol) -> None:
    print(quackable.quack())


if __name__ == "__main__":
    call_quack(DuffyDuck())
    call_quack(Human())
