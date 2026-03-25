
def main() -> None:
    # sequence, set, and mapping types
    # We're not saying anything about the type of values within sequence/mapping
    a_list: list = []
    a_tuple: tuple = tuple()

    a_set: set = set()
    a_frozenset: frozenset = frozenset()

    a_dict: dict = {}

    not_a_dict: dict = 123


if __name__ == "__main__":
    main()