## Type Hints:
Type hints allow you to annotate functions and classes you create to indicate the datatype the argument accepts.

**Here are some basic types that you are probably familiar with:**
```
int, float, str, bool
```

Tip: we can obtain the type of any python object using the type() command:
```
x = 5
print(type(x))
<class 'int'>
```
The object `x` therefore has a type int.

---

#### Type hints for containers

Containers include types like: ```list, tuple, set, dict: ```.

Depending on how specific we want to be we can specify the types of the data inside the container:

For example the object ```x = [5, 10, 13, 14]``` is of type: ```list[int]```. Meaning it is a list of integers. We could have also simply defined it is as a ```list```.

---

#### Special type hints

Included in the Python typing package are special type hints that represent

- `Any`: Represents a variable of any type.
- `Union`: Indicates that a variable can have one of several types.

To use these type hints you'll need to import them, for example:

```
TODO from typing import....
Then show an example use of it.
```

---

### How to add type hints to functions
Functions and classes are often defined with type hints.

Here is an example of a simple function with type hints added:

```
def degrees_to_kelvin(temp_degrees: float) -> float:
  """Convert a temperature from units degrees to kelvin"""
    return TODO
```

- The input parameter `temp_degrees` is assigned a type float.
- The output of the function shown by what comes after the `->` is also a float.

---

#### Type hints when returning multiple objects

If you have a function that returns multiple objects, these will be returned as a tuple, you can also add type hints to reflect the 2 or more objects you return. 

```
def add_and_multiply(x: float, y: float) -> tuple[float, float]:
    """
    Adds and multiplies two numbers.

    Parameters
    ----------
    x: float 
      The first number.
    y: float
      The second number.

    Returns
    -------
    result_sum: float
      The sum of the inputs x and y. 

    result_product: float
      The products of the inputs x and y. 
    """
    result_sum = x + y
    result_product = x * y
    return result_sum, result_product

# Example usage:
the_sum, the_product = add_and_multiply(3.0, 4.0)
print(f"Sum: {the_sum}, Product: {the_product}")

```

Here we specify that two floats will be returned as a tuple: `tuple[float, float]`. 

Note that we can't use type hints alone to specify which object comes out first, but we can do that by documenting the function. 

---

#### Type hints for 3rd party library objects
TODO - pd.dataframe






---


### Question: What should the type hints be for the function below?

```
def multiply_two_numbers(number_1, number_2):
    return number_1 * number_2
```

<details>
  <summary>Click to reveal answer</summary>
  ```
  def multiply_two_numbers(number_1: float, number_2: float) -> float:
      return number_1 * number_2
  ```

  You may have been tempted to write `int` or `Union[float, int]`. But in this case, by saying we can take a float, we imply we can take an int.

</details>

---


### Exercise: Add Type Hints

[Download this python script](https://raw.githubusercontent.com/RMCrean/practical-python-for-scientists/master/docs/day2/type_hints_exercise/add_type_hints.py) and add type hints to the functions inside. 

The answers will be added at the end of the day. 

---

### Summary:

Remember, type hints are a way to provide hints to developers and users about the expected types of different objects in your code. They are not enforced by the Python interpreter at runtime. If you want to enforce type checking you can look into tools like [mypy](https://mypy-lang.org/). 

---

### Further Reading:

- [A type hints introduction/tutorial](https://dagster.io/blog/python-type-hinting)
- [Video: 5 Reasons Why You Should Use Type Hints In Python](https://www.youtube.com/watch?v=dgBCEB2jVU0)
