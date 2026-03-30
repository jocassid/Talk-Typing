

from typing import Callable

IntFunction = Callable[..., int]

def add_two(a: int, b: int) -> int: return a + b
def add_three(a: int, b: int, c: int) -> int: return a + b + c
def str_len(a: str) -> int: return len(a.strip())

def div_two(a: int, b: int) -> float: return a / b


def main() -> None:
    int_functions: list[IntFunction] = [
        add_two,
        add_three,
        str_len,
        div_two,
    ]


if __name__ == "__main__":
    main()
