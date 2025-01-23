from Lynx.utils.compile.language import Language
from Lynx.utils.constants import ALLOWED_STANDARDS


class Cpp(Language):
    def __init__(self) -> None:
        standards = ALLOWED_STANDARDS
        super().__init__(standards)

    def get_environment(self) -> None: ...

    def compile_to_executive(self, source: str, std: str, args: list) -> str:
        """Compiles the cpp source code to executive.

        Args:
            source: (str) The absolute route of the source.
            std: (str) The name of language standard.
            args: (list) The list of arguments for the compiler or interpreter.
        Returns:
            The absolute route of executive.
        """
        raise NotImplementedError()
