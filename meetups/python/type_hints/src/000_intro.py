from typing import List, Optional


class ProgrammingLanguage:
    def __init__(self, name: str, low_level: bool, stable_version: Optional[int] = None) -> None:
        self._name = name
        self._stable_version = stable_version
        self._low_level = low_level

    @staticmethod
    def basic_types() -> List[str]:
        return ["int", "float", "str"]
