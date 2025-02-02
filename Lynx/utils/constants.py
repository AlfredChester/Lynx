import os

VERSION = "2.0.1b4"

# Some directories
LYNX_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTLIB_ROOT = os.path.join(LYNX_ROOT, "..", "testlib")
TEMPLATES_ROOT = os.path.join(LYNX_ROOT, "templates")
CPP_TEMPLATES_ROOT = os.path.join(TEMPLATES_ROOT, "cpp")

# Standards
CPP_STANDARDS = ["c++98", "c++03", "c++11", "c++14", "c++17"]

# Testlib checkers and validators
CHECKERS = [
    "custom",
    "nyesno",
    "ncmp",
    "casencmp",
    "lcmp",
    "rncmp",
    "yesno",
    "dcmp",
    "hcmp",
    "pointscmp",
    "rcmp",
    "fcmp",
    "rcmp9",
    "rcmp4",
    "wcmp",
    "rcmp6",
    ".gitignore",
    "casewcmp",
    "acmp",
    "icmp",
    "pointsinfo",
    "uncmp",
    "caseicmp",
]
VALIDATORS = [
    "custom",
    "validate-using-testset-and-group",
    "undirected-graph-validator",
    "bipartite-graph-validator",
    "nval",
    "undirected-tree-validator",
    "sval",
    "ival",
    "case-nval",
]

SUPPORTED_OJ = ["luogu", "hydro", "qdu"]
