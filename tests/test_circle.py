import unittest
import math
from geometric_lib import circle

class TestCircle(unittest.TestCase):
    def test_area_basic(self):
        self.assertAlmostEqual(circle.area(1), math.pi, places=6)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5**2, places=6)

    def test_perimeter_basic(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi, places=6)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5, places=6)

    def test_zero(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            circle.area(-1)
        with self.assertRaises(ValueError):
            circle.perimeter(-2)

    def test_type_raises(self):
        for bad in ("3", None, [], {}):
            with self.assertRaises(TypeError):
                circle.area(bad)
            with self.assertRaises(TypeError):
                circle.perimeter(bad)

if __name__ == "__main__":
    unittest.main()
