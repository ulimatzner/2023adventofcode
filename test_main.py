from unittest import TestCase
import day1 as today


class Test(TestCase):
    def test_main(self):
        expected = 142
        actual = today.code.solve("test_input.txt")
        self.assertEqual(expected, actual)
