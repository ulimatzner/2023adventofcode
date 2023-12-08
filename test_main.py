from unittest import TestCase
import day0 as today


class Test(TestCase):
    def test_main(self):
        expected = 0
        actual = today.code.solve("test_input.txt")
        self.assertEqual(expected, actual)
