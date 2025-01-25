import yaml
import os


# Used to manage the range of variables more easily
# It will be replaced by some features of cyaron in the future.
class SubtaskManager: ...


class CppProblemConfig:
    def __init__(self, problem_path: str):
        self.problem_path = problem_path
        self.problem_config_path = os.path.join(problem_path, "problem.yaml")
        self.testdata_config_path = os.path.join(
            problem_path, "testdata", "config.yaml"
        )

    def init_configs(
        self, standard, testcase, time_limit, memory_limit, no_checker
    ): ...
