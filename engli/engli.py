"""Engli, Natural Programming Language, English readable python language."""
import os
import sys

from errors import FileDoesNotEndWithENGLI

from translate.translate_unittests import unittests
from translate.translate_loops import loops
from translate.translate_comparisons import comparisons


TRANSLATORS = [unittests, loops, comparisons]


def translate(code):
    """Translate a piece of engli code into python code.

    Args:
        code (str): original engli code.

    Returns:
        str. output python code.
    """
    for translator in TRANSLATORS:
        code = translator(code)

    return code


def run(engli_path, should_execute=True):
    """Create and run a .py file from a .engli file.

    Args:
        engli_path (str): path to a .engli file.
        should_execute (bool): whether to execute new .engli file or not.
    """
    py_path = engli_path[:-1]

    if not engli_path.endswith(".engli"):
        raise FileDoesNotEndWithENGLI(engli_path)

    with open(py_path, "w") as py_file, open(engli_path, "r") as engli_file:
        engli_code = engli_file.read()
        py_code = translate(engli_code)
        py_file.write(py_code)

    if should_execute:
        os.system("python %s" % py_path)

if __name__ == '__main__':
    run(sys.argv[1])  # TODO: Make it possible to translate a project.
