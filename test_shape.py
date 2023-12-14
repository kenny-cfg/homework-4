import unittest

from shape import Square


class TestShape(unittest.TestCase):
    def test_square(self):
        s = Square(6)

        perimeter = s.calc_perimeter()
        area = s.calc_area()

        self.assertEqual(perimeter, 24)
        self.assertEqual(area, 36)

    def test_rectangle(self):
        r = Rectangle(6, 4)

        perimeter = r.calc_perimeter()
        area = r.calc_area()

        self.assertEqual(perimeter, 20)
        self.assertEqual(area, 24)


if __name__ == '__main__':
    unittest.main()
