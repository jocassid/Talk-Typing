
from typing import Optional


def greeting(name: str | None = None) -> None:
    name = name or 'stranger'
    print(f'Hello, {name}!')


def greeting_before_py3_10(name: Optional[str] = None) -> None:
    greeting(name)


def main() -> None:
    greeting()
    greeting(None)
    greeting('Alice')

    greeting_before_py3_10()
    greeting_before_py3_10('Bob')
    greeting_before_py3_10(['Alice', 'Bob'])

    not_optional: str = None


if __name__ == "__main__":
    main()
