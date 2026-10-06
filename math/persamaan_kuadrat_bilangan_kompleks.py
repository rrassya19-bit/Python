from __future__ import annotations

import math


def akar_kuadrat(a: int, b: int, c: int) -> tuple[float, float] | float | str:
    """
    diberikan koefisien numerik a, b dan c,
    menghitung akar untuk setiap persamaan kuadrat dalam bentuk ax^2 + bx + c

    >>> akar_kuadrat(a = 1,b =  3,c = -4)
    (1.0, -4.0)

    >>> akar_kuadrat(5, 6, 1)
    (-0.2, -1.0)

    >>> akar_kuadrat(-1, 2, 3)
    (-1.0, 3.0)

    >>> akar_kuadrat(0, -2, 3)
    Traceback (most recent call last):
    ...
    ValueError: Koefisien a tidak boleh 0
    """

    if a == 0:
        raise ValueError("Koefisien a tidak boleh 0")

    delta = b * b - 4 * a * c

    if delta > 0:
        akar_1 = (-b + math.sqrt(delta)) / (2 * a)
        akar_2 = (-b - math.sqrt(delta)) / (2 * a)

        return akar_1, akar_2

    elif delta == 0:
        return -b / (2 * a)

    else:
        msg: str = "persamaanya menjadi imajiner"
        return msg


def main() -> None:
    solusi1, solusi2 = akar_kuadrat(a=1, b=3, c=4)
    print(f"solusi adalah {solusi1} dan {solusi2}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
