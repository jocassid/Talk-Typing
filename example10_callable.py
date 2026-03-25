
from typing import Callable

# Callable[[arg_type1, arg_type2], return_type]
Filter = Callable[[str], bool]

def lowercase_filter(text_in: str) -> bool:
    return text_in == text_in.lower()

def less_than_5_letters(text_in: str) -> bool:
    return len(text_in) < 5

def add(a: int, b: int) -> int:
    return a + b

def blurgh(text_in: str, *args, **kwargs) -> bool:
    return any(a in text_in for a in args)


def main() -> None:
    filters: list[Filter] = [lowercase_filter, less_than_5_letters]
    not_a_filter: Filter = add
    filter_with_args: Filter = blurgh

if __name__ == "__main__":
    main()
