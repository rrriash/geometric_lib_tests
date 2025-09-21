import unittest
from geometric_lib import square

class TestSquare(unittest.TestCase):
    # Позитивные
    def test_area_basic(self):
        self.assertEqual(square.area(4), 16)
        self.assertAlmostEqual(square.area(2.5), 6.25, places=6)

    def test_perimeter_basic(self):
        self.assertEqual(square.perimeter(4), 16)
        self.assertAlmostEqual(square.perimeter(2.5), 10.0, places=6)

    # Граничные
    def test_zero(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    # Негативные
    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            square.area(-1)
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_type_raises(self):
        for bad in ("3", None, [], {}):
            with self.assertRaises(TypeError):
                square.area(bad)
            with self.assertRaises(TypeError):
                square.perimeter(bad)

if __name__ == "__main__":
    unittest.main()
