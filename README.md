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
