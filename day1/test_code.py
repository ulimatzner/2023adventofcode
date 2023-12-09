from unittest import TestCase
import code


class Test(TestCase):
    def test_solve(self):
        expected = 142
        actual = code.solve("test_input.txt")
        self.assertEqual(expected, actual)
