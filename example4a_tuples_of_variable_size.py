
IntTuple = tuple[int, ...]
EmptyTuple1 = tuple[()]

# Same as tuple[int, str, Any], but mypy doesn't like this declaration
IntStrAny = tuple[int, str, ...]

def main() -> None:
    a: IntTuple = (1, 2)
    b: IntTuple = (3, 4, 5)
    c: IntTuple = ()
    d: IntTuple = (1, 2, 'foo')

    e: EmptyTuple1 = ()
    f: EmptyTuple1 = (1, 2, 3)

    g: IntStrAny = (1, 'foo')
    h: IntStrAny = (1, 'foo', 2)
    i: IntStrAny = (1, 'foo', 2, 'bar')


if __name__ == "__main__":
    main()