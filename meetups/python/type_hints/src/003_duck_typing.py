class DuffyDuck:
    def quack(self):
        return "<natural quack>"


class Human:
    def quack(self):
        return "<faked, yet quack>"


def call_quack(o):
    print(o.quack())


if __name__ == "__main__":
    call_quack(DuffyDuck())
    call_quack(Human())
