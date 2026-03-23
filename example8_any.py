
from typing import Any

def main():
    cache: dict[str, Any] = {
        'user_profile': {
            'username': 'carol',
            'theme_default': 'dark',
        },
        'cart': [
            {'product_id': 123, 'quantity': 2},
            {'product_id': 456, 'quantity': 1},
        ]
    }
    cache[5] = 'blurgh'  # wrong key type


if __name__ == "__main__":
    main()
