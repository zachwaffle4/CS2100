import unittest
from first_lecture import get_area_of_rectangle, get_area_of_triangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the rectangle functions."""
    def test_area_3_by_4(self) -> None:
        """3 by 4 rectangle"""
        w: int = 3
        h: int = 4

        self.assertEqual(get_area_of_rectangle(w, h), 12)

class TestTriangle(unittest.TestCase):
    """Unit tests for the triangle functions."""
    def test_area_3_by_4(self) -> None:
        """3 by 4 triangle"""
        b: int = 3
        h: int = 4

        self.assertEqual(get_area_of_triangle(b, h), 6)

if __name__ == '__main__':
    unittest.main()
