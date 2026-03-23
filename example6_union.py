
from decimal import Decimal
from fractions import Fraction
from typing import Dict

numeric = int | float | complex | Fraction | Decimal

# For Python < 3.10
# from typing import Union
# numeric = Union[int, float, complex, Fraction, Decimal]

def add_numeric(a: numeric, b: numeric) -> numeric:
    return a + b

def show_operation(
        label1: str, value1: numeric, label2: str, value2: numeric,
        value_sum: numeric
) -> None:
    print(
        f'{value1!r} ({label1}) + {value2} ({label2}) = '
        f'{value_sum!r} ({type(value_sum).__name__})'
    )
def main():
    sample_values: Dict[str, numeric] = {
        'int': 1,
        'float': 2.5,
        'complex': 1 + 2j,
        'fraction': Fraction(1, 2),
        'decimal': Decimal('0.1')
    }

    for label1, value1 in sample_values.items():
        for label2, value2 in sample_values.items():
            try:
                value_sum = value1 + value2
            except TypeError:
                print(f'Cannot add {label1} and {label2}')
            else:
                show_operation(label1, value1, label2, value2, value_sum)

if __name__ == "__main__":
    main()