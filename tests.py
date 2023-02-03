import unittest

from main import Number


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        rez = Number(5) + Number(10)
        self.assertEqual(rez.number, 15)
        # TODO: Fix this
        self.assertEqual(rez, 15)

    def test_noname(self):
        with self.assertRaises(ZeroDivisionError):
            Number(15) / Number(0)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
