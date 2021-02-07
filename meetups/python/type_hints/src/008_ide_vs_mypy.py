from typing import Optional


class Language:
    shortname: Optional[str]


class CSharp(Language):
    shortname = "C#"


class JavaScript(Language):
    shortname = "JS"


class C(Language):
    shortname = None


def get_language_shortname(lang: Language) -> str:
    return lang.shortname


def get_upper_shortname(lang: Language) -> str:
    return get_language_shortname(lang).upper()
