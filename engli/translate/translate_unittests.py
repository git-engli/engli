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
