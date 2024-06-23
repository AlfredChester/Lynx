suffix_of_language = {"cpp": [".cpp", ".cxx", ".cc", ".c++", ".C"], "rust": [".rc"]}


class LanguageDeterminationError(Exception):
    """Exception used when the language of given source cannot be determined."""


class Language(object):
    def __init__(self, standards: list) -> None:
        self.standards = standards

    def getEnvironment(self) -> None:
        """Get the (compiling) environment for this language"""
        ...

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
