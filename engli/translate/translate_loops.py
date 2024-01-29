import re


UNTIL = "until (.+):"
AS_LONG_AS = "as long as (.+):"
TIMES = "(.+) times:"
DO_WHILE = NotImplemented  # TODO
FOREACH = "foreach"
FOR_EACH = "for each"
FOR_EVERY = "for every"


def loops(code):
    """Translate loops  piece of codes from engli to python.

    Args:
        code (str): engli code to translate.

    Returns:
        str. python code.

    Note:
        Order of execution of these regex code is important!
        From less specific to more specific.
    """
    code = re.sub(UNTIL, r"while not \1:", code)
    code = re.sub(AS_LONG_AS, r"while \1:", code)
    code = re.sub(TIMES, r"for _ in xrange(\1):", code)
    code = re.sub(FOR_EACH, r"for", code)
    code = re.sub(FOREACH, r"for", code)
    code = re.sub(FOR_EVERY, r"for", code)
    return code
