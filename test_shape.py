import unittest

from shape import Square


class TestShape(unittest.TestCase):
    def test_square(self):
        s = Square(6)

        perimeter = s.calc_perimeter()
        area = s.calc_area()

        self.assertEqual(perimeter, 24)
        self.assertEqual(area, 36)


if __name__ == '__main__':
    unittest.main()
