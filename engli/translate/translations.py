import re

# Asserts
ASSERT_THAT_STAR = "assert that (.+)"
ASSERT_THAT_RAISES = "assert that (.+) raises (.+)"
ASSERT_RAISES = "assert raises (.+):"

# Lists
ASSERT_THAT_IS_ITERABLE = "assert that (.+) is iterable"
ASSERT_THAT_CONTAINS_IN_ORDER = "assert that (.+) contains (.+) in order"

# Shoulds
SHOULD_BE_EQ = "(.+) should be equal to (.+)"
SHOULD_BE_GTE = "(.+) should be greater than or equal to (.+)"
SHOULD_BE_GT = "(.+) should be greater than (.+)"
SHOULD_BE_LTE = "(.+) should be less than or equal to (.+)"
SHOULD_BE_LT = "(.+) should be less than (.+)"
SHOULD_BE_NE = "(.+) should not be equal to (.+)"
SHOULD_BE_BETWEEN = "(.+) should be between (.+) and (.+)"
SHOULD_BE = "(.+) should be (.+)"


def unittests(code):
    """Translate unit-test piece of codes from engli to python.

    Args:
        code (str): engli code to translate.

    Returns:
        str. python code.
    """
    # LISTS
    code = re.sub(ASSERT_THAT_CONTAINS_IN_ORDER,
                  r"self.assertTrue(any(\1[i:i+len(\2)]==\2 "
                  r"for i in xrange(len(\1)-len(\2)+1)))",
                  code)

    code = re.sub(ASSERT_THAT_IS_ITERABLE,
                  r"import collections; self.assertTrue(isinstance(\1, "
                  r"collections.Iterable))",
                  code)
    # GENERAL
    code = re.sub(ASSERT_THAT_RAISES,
                  r"self.assertRaises(\1, \2)",
                  code)

    code = re.sub(ASSERT_RAISES,
                  r"with self.assertRaises(\1):",
                  code)

    code = re.sub(ASSERT_THAT_STAR, r"self.assertTrue(\1)", code)

    # SHOULDS
    code = re.sub(SHOULD_BE_EQ, r"assert (\1 == \2)", code)
    code = re.sub(SHOULD_BE_NE, r"assert (\1 != \2)", code)
    code = re.sub(SHOULD_BE_GTE, r"assert (\1 >= \2)", code)
    code = re.sub(SHOULD_BE_GT, r"assert (\1 > \2)", code)
    code = re.sub(SHOULD_BE_LTE, r"assert (\1 <= \2)", code)
    code = re.sub(SHOULD_BE_LT, r"assert (\1 < \2)", code)
    code = re.sub(SHOULD_BE_BETWEEN, r"assert (\2 <= \1 <= \3)", code)
    code = re.sub(SHOULD_BE, r"assert (\1 is \2)", code)

    return code

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




GTE = "(\w) is greater than or equal to (\w)"
GT = "(\w) is greater than (\w)"
EQ = "(\w) is equal to (\w)"
NE = "(\w) is not equal to (\w)"
LT = "(\w) is less than (\w)"
LTE = "(\w) is less than or equal to (\w)"
BETWEEN = "(\w) is between (\w) and (\w)"


def comparisons(code):
    """Translate comparison piece of codes from engli to python.

    Args:
        code (str): engli code to translate.

    Returns:
        str. python code.

    Note:
        Order of execution of these regex code is important!
        From less specific to more specific.
    """
    code = re.sub(GTE, r"\1 >= \2", code)
    code = re.sub(GT, r"\1 > \2", code)

    code = re.sub(EQ, r"\1 == \2", code)
    code = re.sub(NE, r"\1 != \2", code)

    code = re.sub(LTE, r"\1 <= \2", code)
    code = re.sub(LT, r"\1 < \2", code)

    code = re.sub(BETWEEN, r"\2 <= \1 <= \3", code)

    return code
