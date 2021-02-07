from typing import Any, Callable, Dict, Iterable, Literal, Optional, Type, Union


###################################
# Any
###################################


def get_val(d: dict, key: str) -> Any:
    return d[key]


###################################
# Dict
###################################


language2version: Dict[str, int] = dict()
language2version["Python 3"] = 3
language2version["Python 2"] = 2


###################################
# Union
###################################


def is_big(num: Union[int, float]) -> bool:
    if num >= 1000000000:
        return True
    return False


###################################
# Optional
###################################


def ban_user(username: str, reason: Optional[str]) -> None:
    if reason is None:
        print(f"User {username} was banned.")
    else:
        print(f"User {username} was banned for {reason}.")


###################################
# Iterable
###################################


def print_uppercase(it: Iterable[str]) -> None:
    for el in it:
        print(el.upper())


print_uppercase(["a", "b", "c"])
print_uppercase({"a", "a", "b", "c"})
print_uppercase(
    (char for char in "abc")
)


###################################
# Type Alias
###################################


ID = Union[int, str]


def next_id(cur_id: ID) -> int:
    return int(cur_id) + 1


###################################
# Literal (Python 3.8 and above)
###################################


def sort(it: Iterable[str], order: Literal["asc", "desc"]) -> Iterable[str]:
    if order == "asc":
        return sorted(it)
    return sorted(it, reverse=True)


###################################
# Callable
###################################

def is_upper(val: str) -> bool:
    return val.isupper()


def is_lower(val: str) -> bool:
    return val.islower()


def check_case(val: str, check_meth: Callable[[str], bool]) -> bool:
    print("Checking case")
    return check_meth(val)


check_case("string", is_lower)
check_case("STRING", is_upper)


###################################
# Type
###################################


class Liquid:
    def __init__(self, liters: int) -> None:
        self.liters = liters


class Water(Liquid):
    """Common Water"""


class Wine(Liquid):
    """Precious Wine"""


def transform(val: Liquid, to: Type[Liquid]) -> Liquid:
    return to(val.liters)


water = Water(100)
wine = transform(water, Wine)
