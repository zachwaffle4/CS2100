import unittest

def get_area_of_rectangle(width: int, height: int) -> int:
    """Returns the area of a rectangle.
    Parameters
    ----------
    width : int
        The width of the rectangle
    height: int
        The height of the rectangle
    Returns
    -------
    int
        The area of the rectangle
    Raises
    ------
    ValueError
        If width or height is negative
    """
    if width < 0 or height < 0:
        raise ValueError("Rectangle dimensions cannot be negative")
    return width * height

def get_area_of_triangle(base: float | int, height: float | int) -> float:
    """
    Returns the area of a triangle.
    
    :param base: Length of one side of the triangle.
    :param height: Perpendicular height from [base] to third vertex.
    :return: Area of the triangle.
    :raises ValueError: If base or height are negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Triangle dimensions cannot be negative")
    return 0.5 * base * height
