from typing import Any, Protocol

class Event: ...

class EventHandler(Protocol):
    def __call__(self, event: Event, *args: str, log_event: bool = False) -> bool: ...

def handle_click(event: Event, *args: str, log_event: bool = False) -> bool:
    all_args = "{} {} {}".format(
        event,
        [repr(a) for a in args],
        f"{log_event=!r}",
    )
    print(f'handling click {all_args}')
    if log_event:
        print(f'logging click {all_args}')
    return True


def main() -> None:
    e1 = Event()

    h1: EventHandler = handle_click
    h1(e1)
    h1(e1, 'foo', 'bar', log_event=True)
    h1(e1, 'yadayada', )
    h1(e1, 1, 2)
    h1(e1, propagate_event=False)





if __name__ == "__main__":
    main()
