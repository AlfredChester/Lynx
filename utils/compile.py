import os

from typing import Optional


class LanguageDeterminationError(Exception):
    """Exception used when the language of given source cannot be determined."""


class Language(object):
    def __init__(self, standards: list) -> None:
        self.standards = standards

    def compileToExecutive(self, source: str, std: str, args: list) -> str:
        """Compiles the source code to executive.
        Args:
            source: (str) The absolute route of the source.
            std: (str) The name of language standard.
            args: (list) The list of arguments for the compiler or interpreter.
        Returns:
            The absolute route of executive.
        """
        raise NotImplementedError()


class CPP(Language):
    def __init__(self) -> None:
        standards = ["c++98", "c++03", "c++11", "c++14", "c++17"]
        super().__init__(standards)

    def compileToExecutive(self, source: str, std: str, args: list) -> str:
        """Compiles the cpp source code to executive.
        Args:
            source: (str) The absolute route of the source.
            std: (str) The name of language standard.
            args: (list) The list of arguments for the compiler or interpreter.
        Returns:
            The absolute route of executive.
        """


def getLanguage(source: str) -> str:
    source_suffix = os.path.splitext(source)[-1]
    if source_suffix == " ":
        raise LanguageDeterminationError()
    suffix_of_language = {"cpp": [".cpp", ".cxx", ".cc", ".c++", ".C"]}
    for language, suffix in suffix_of_language:
        if source_suffix in suffix:
            return language
    raise LanguageDeterminationError()


def compile(source: str, language: Optional[str], std: str, args: list) -> int:
    if language is None:
        language = getLanguage(source)
    if language == "cpp":
        CPP().compileToExecutive(source)
    else:
        raise NotImplementedError(
            f"{language} has not been supported yet. Please start an issue if you need."
        )
