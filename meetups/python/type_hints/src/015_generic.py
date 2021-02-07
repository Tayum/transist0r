from typing import Any, Generic, List, Optional, TypeVar


###################################
# Models
###################################


ModelT = TypeVar("ModelT", bound="Model")


class Model:
    def __init__(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


class Whisky(Model):
    single_malt: bool


class Wine(Model):
    color: str


###################################
# Repositories
###################################


class Repository(Generic[ModelT]):
    def read(self) -> List[ModelT]:
        ...

    def read_one(self, id: int) -> Optional[ModelT]:
        ...

    def add_one(self, val: dict) -> None:
        ...


class WhiskyRepository(Repository[Whisky]):
    """Silky Whisky"""


class WineRepository(Repository[Wine]):
    """Charming Wine"""


if __name__ == "__main__":
    whisky_repo = WhiskyRepository()
    whisky = whisky_repo.read_one(1)
    if whisky:
        print(whisky.single_malt)

    wine_repo = WineRepository()
    wines = wine_repo.read()
    for wine in wines:
        print(wine.color)
