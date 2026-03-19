# Talk-Typing

A talk about type annotations in python

## Why Are Type Annotations Helpful?

1. Avoid type mistakes (i.e. passing the wrong type of arguments to a function)
2. Make code more readable
3. Tools such as PyCharm or VSCode will show function/method signature if you 
hover over the call.  If you add type annotations of the arguments and return 
value(s), the types will be shown in the pop-up
4. When building a new function, it helps if you can define the type of data 
going in (arguments) and out (return values).


## Notes

1. `ruff` doesn't do type checking.  Use `mypy` instead.  `pip install mypy`

## History of Type Annotations

### Python 3.5

* Introduction of standard library `typing`

### Python 3.9

* Eliminated the need for `Dict`, `List`, `Set`, `FrozenSet`, `Tuple`, `Type` 
aliases.  Can now use `list[int]` instead of `List[int]`
* Eliminated the need for aliases to types in other standard library modules:
  * `collections`: `DefaultDict`, `OrderedDict`, `ChainMap`, `Counter`, `Deque`
  * `re`: `Match`, `Pattern`
  


## References

* https://typing.python.org/en/latest/spec/annotations.html
* https://leapcell.medium.com/explaining-python-type-annotations-a-comprehensive-guide-to-the-typing-module-87d9e3599d59 Note: This uses < Python3.9 code
* 