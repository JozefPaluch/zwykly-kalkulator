"""
Moduł z podstawowymi funkcjami kalkulatora.
"""


def add(a: int, b: int) -> int:
    """
    Zwraca sumę dwóch liczb całkowitych.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Zwraca różnicę dwóch liczb całkowitych.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Zwraca iloczyn dwóch liczb całkowitych.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Zwraca iloraz dwóch liczb.
    Zakłada, że b != 0.
    """
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b
