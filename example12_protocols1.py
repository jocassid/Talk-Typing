from typing import Protocol


class Combiner(Protocol):
    def __call__(self, multiple: float, *vals: str, max_len: int | None = None) -> str:
        ...

def batch_proc(data: list[str], cb_results: Combiner) -> str:
    for item in data:
        ...
    return 'yadayada'

def good_cb(multiple: float, *vals: str, max_len: int | None = None) -> str:
    """Notice this has a default value for max_len"""
    return 'foo'

def bad_cb(*vals: str, max_items: int | None) -> str:
    """max_items instead of max_len and no default value"""
    return 'bar'


def main() -> None:
    c1: Combiner = good_cb
    c1(3.14,'a', 'b', max_len=2)
    c1(3.75, max_len=5)
    batch_proc([], c1)

    c1('a', max_len=2, a=15)

    c2: Combiner = bad_cb
    batch_proc([], c2)

if __name__ == "__main__":
    main()
