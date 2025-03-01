mport unittest
from triangles import classify_triangle

class TestTriangles(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")

    def test_not_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a Triangle")
        self.assertEqual(classify_triangle(10, 2, 3), "Not a Triangle")

    def test_invalid(self):
        self.assertEqual(classify_triangle(-1, 2, 3), "Invalid")
        self.assertEqual(classify_triangle(0, 2, 3), "Invalid")

if __name__ == '__main__':
    unittest.main()
