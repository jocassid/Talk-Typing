

def main() -> None:
    # numeric types
    an_int: int = 10
    a_float: float = 10.0
    a_complex: complex = 5 + 10j

    # boolean type
    a_bool: bool = True

    # text and binary sequence types
    a_str: str = 'foo'
    some_bytes: bytes = b'foo'
    a_bytearray: bytearray = bytearray()
    a_memory_view: memoryview = memoryview(b'foo')

    result: int = "A suffusion of yellow"  # TYPE ERROR

if __name__ == "__main__":
    main()