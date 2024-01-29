import re


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
