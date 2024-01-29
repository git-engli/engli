from unittest import TestCase
from translate.translate_comparisons import comparisons


class ComparisonsTest(TestCase):
    def test_gte(self):
        code = "if x is greater than or equal to foo() + 4: print foo()"
        expected = "if x >= foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_gt(self):
        code = "if x is greater than foo() + 4: print foo()"
        expected = "if x > foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_lt(self):
        code = "if x is less than foo() + 4: print foo()"
        expected = "if x < foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_lte(self):
        code = "if x is less than or equal to foo() + 4: print foo()"
        expected = "if x <= foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_eq(self):
        code = "if x is equal to foo() + 4: print foo()"
        expected = "if x == foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_ne(self):
        code = "if x is not equal to foo() + 4: print foo()"
        expected = "if x != foo() + 4: print foo()"
        actual = comparisons(code)
        self.assertEqual(expected, actual)

    def test_between(self):
        code = "if x is between 0 and 10: print x"
        expected = "if 0 <= x <= 10: print x"
        actual = comparisons(code)
        self.assertEqual(expected, actual)
