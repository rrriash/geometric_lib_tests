import math

def _ensure_number(x):
    if not isinstance(x, (int, float)):
        raise TypeError("radius must be a number")
    return float(x)

def area(r):
    """Вычисляет площадь круга: πr²
    
    Args:
        r (float): радиус

    Returns:
        float: площадь круга
    """
    r = _ensure_number(r)
    if r < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * r * r

def perimeter(r):
    """Вычисляет длину окружности: 2πr
    
    Args:
        r (float): радиус

    Returns:
        float: длина окружности
    """
    r = _ensure_number(r)
    if r < 0:
        raise ValueError("radius must be non-negative")
    return 2 * math.pi * r

