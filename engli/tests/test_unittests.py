from unittest import TestCase

from translate.translate_comparisons import comparisons
from translate.translate_unittests import unittests as ut


class UnittestCase(TestCase):
    def test_assertThat(self):
        code = "assert that x == y"
        expected = "self.assertTrue(x == y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected,
                          actual)

    def test_assertThatIsEqualTo(self):
        code = "assert that x is equal to y"
        expected = "self.assertTrue(x == y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsNotEqualTo(self):
        code = "assert that x is not equal to y"
        expected = "self.assertTrue(x != y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsGreaterThan(self):
        code = "assert that x is greater than y"
        expected = "self.assertTrue(x > y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsGreaterThanOrEqualTo(self):
        code = "assert that x is greater than or equal to y"
        expected = "self.assertTrue(x >= y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsLessThan(self):
        code = "assert that x is less than y"
        expected = "self.assertTrue(x < y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsLessThanOrEqualTo(self):
        code = "assert that x is less than or equal to y"
        expected = "self.assertTrue(x <= y)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertThatIsBetween(self):
        code = "assert that x is between 0 and 9"
        expected = "self.assertTrue(0 <= x <= 9)"
        actual = ut(comparisons(code))
        self.assertEquals(expected, actual)

    def test_assertIsIterable(self):
        code = "assert that x is iterable"
        expected = "import collections; " \
                   "self.assertTrue(isinstance(x, collections.Iterable))"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertContainsInOrder(self):
        code = "assert that [1, 2, 3] contains [2, 3] in order"
        eval(ut(code))
        with self.assertRaises(AssertionError):
            code = "assert that [1, 2, 3] contains [1, 3] in order"
            eval(ut(code))

    def test_assertRaises(self):
        code = "assert raises MeowException:"
        expected = "with self.assertRaises(MeowException):"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatRaises(self):
        code = "assert that foo raises MeowException"
        expected = "self.assertRaises(foo, MeowException)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assert_is_not(self):
        code = "assert that x is not 4"
        expected = "self.assertTrue(x is not 4)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_be(self):
        code = "x should be 3"
        expected = "assert (x is 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_eq(self):
        code = "x should be equal to 3"
        expected = "assert (x == 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_ne(self):
        code = "x should not be equal to 3"
        expected = "assert (x != 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_lte(self):
        code = "x should be less than or equal to 3"
        expected = "assert (x <= 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_lt(self):
        code = "x should be less than 3"
        expected = "assert (x < 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_gte(self):
        code = "x should be greater than or equal to 3"
        expected = "assert (x >= 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_gt(self):
        code = "x should be greater than 3"
        expected = "assert (x > 3)"
        actual = ut(code)
        self.assertEqual(expected, actual)

    def test_should_between(self):
        code = "x should be between 0 and 9"
        expected = "assert (0 <= x <= 9)"
        actual = ut(code)
        self.assertEqual(expected, actual)
