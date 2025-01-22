from Lynx.utils.compile.language import Language

allowed_standards = ["c++98", "c++03", "c++11", "c++14", "c++17"]


class Cpp(Language):
    def __init__(self) -> None:
        standards = allowed_standards
        super().__init__(standards)

    def getEnvironment(self) -> None: ...

    def compileToExecutive(self, source: str, std: str, args: list) -> str:
        """Compiles the cpp source code to executive.

        Args:
            source: (str) The absolute route of the source.
            std: (str) The name of language standard.
            args: (list) The list of arguments for the compiler or interpreter.
        Returns:
            The absolute route of executive.
        """
        raise NotImplementedError()
