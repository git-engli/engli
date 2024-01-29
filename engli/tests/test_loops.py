from unittest import TestCase
from translate.translate_loops import loops


class LoopsTest(TestCase):
    def test_until(self):
        code = "until x == 4: print x; x += 1"
        expected = "while not x == 4: print x; x += 1"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_as_long_as(self):
        code = "as long as x == 4: print x; x += 1"
        expected = "while x == 4: print x; x += 1"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_times_number(self):
        code = "4 times: print x; x += 1"
        expected = "for _ in xrange(4): print x; x += 1"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_times_expression(self):
        code = "foo() times: print x; x += 1"
        expected = "for _ in xrange(foo()): print x; x += 1"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_do_while(self):
        return NotImplemented  # TODO

    def test_foreach(self):
        code = "foreach x in y: print x"
        expected = "for x in y: print x"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_for_each(self):
        code = "for each x in y: print x"
        expected = "for x in y: print x"
        actual = loops(code)
        self.assertEqual(expected, actual)

    def test_for_every(self):
        code = "for every x in y: print x"
        expected = "for x in y: print x"
        actual = loops(code)
        self.assertEqual(expected, actual)
