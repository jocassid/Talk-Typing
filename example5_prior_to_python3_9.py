
from typing import List, Tuple, Set, FrozenSet, Dict

def main():

    # sequence, set, and mapping types
    # We're not saying anything about the type of values within sequence/mapping
    list_of_ints: List[int] = [1, 2, 3]
    a_tuple: Tuple[bool, int] = (True, 5)

    a_set: Set[int] = {2, 3, 5, 7}
    a_frozenset: FrozenSet[float] = frozenset([0.5, 0.25, 0.125])

    a_dict: Dict[str, int] = {'Ohio': 1803, 'New York': 1788}


if __name__ == "__main__":
    main()