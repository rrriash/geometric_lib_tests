def _ensure_number(x):
    if not isinstance(x, (int, float)):
        raise TypeError("side must be a number")
    return float(x)

def area(a):
    """Вычисляет площадь квадрата: a²

    Args:
        a (float): длина стороны квадрата

    Returns:
        float: площадь квадрата

    Пример:
        >>> area(4)
        16
    """
    a = _ensure_number(a)
    if a < 0:
        raise ValueError("side must be non-negative")
    return a * a

def perimeter(a):
    """Вычисляет периметр квадрата: 4a

    Args:
        a (float): длина стороны квадрата

    Returns:
        float: периметр квадрата

    Пример:
        >>> perimeter(4)
        16
    """
    a = _ensure_number(a)
    if a < 0:
        raise ValueError("side must be non-negative")
    return 4 * a

