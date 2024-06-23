from typing import Optional
from os.path import splitext

from utils.compile.cpp import Cpp
from utils.compile.rust import Rust
from utils.compile.language import *


def getLanguage(source: str) -> str:
    source_suffix = splitext(source)[-1]
    if source_suffix == " ":
        raise LanguageDeterminationError(
            "Recognizing language by content has not been supported yet."
        )
    for language, suffix in suffix_of_language:
        if source_suffix in suffix:
            return language
    raise LanguageDeterminationError(
        "The file extension does not match any language supported."
    )


def compile(source: str, language: Optional[str], std: str, args: list) -> str:
    if language is None:
        language = getLanguage(source)
    if language == "cpp":
        return Cpp().compileToExecutive(source, std, args)
    else:
        raise NotImplementedError(
            f"{language} has not been supported yet. Please start an issue if you need."
        )
