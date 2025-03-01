"""
This module contains a function to classify triangles based on side lengths.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classifies a triangle based on the lengths of its sides.

    Parameters:
        side_a (float): Length of the first side.
        side_b (float): Length of the second side.
        side_c (float): Length of the third side.

    Returns:
        str: Type of the triangle ("Equilateral", "Isosceles", "Scalene", "Not a Triangle", "Invalid").
    """
    if any(side <= 0 for side in (side_a, side_b, side_c)):
        return "Invalid"

    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Not a Triangle"

    if side_a == side_b == side_c:
        return "Equilateral"

    if side_a == side_b or side_b == side_c or side_a == side_c:
        return "Isosceles"

    return "Scalene"
