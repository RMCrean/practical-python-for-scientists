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





#### Type hints for containers

Containers include types like: ```list, tuple, set, dict: ```.

Depending on how specific we want to be we can specify the types of the data inside the container:

For example the object ```x = [5, 10, 13, 14]``` is of type: ```list[int]```. Meaning it is a list of integers. We could have also simply defined it is as a ```list```.

#### Special type hints

Included in the Python typing package are special type hints that represent

- `Any`: Represents a variable of any type.
- `Union`: Indicates that a variable can have one of several types.

To use these type hints you'll need to import them, for example:

```
TODO from typing import....
Then show an example use of it.
```

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

#### Type hints when returning multiple items
TODO - using a tuple.

#### Type hints for 3rd party library objects
TODO - pd.dataframe






##### Some useful extra type hints
These are some extra tips on type hints:

**1. Consider the function:**
```
def multiply_two_numbers(number_1, number_2):
    return number_1 * number_2
```
What should the type hints be here?


<details>
  <summary>Click to reveal answer</summary>
  ```
  def multiply_two_numbers(number_1: float, number_2: float) -> float:
      return number_1 * number_2
  ```

  You may have been tempted to write `int` or `Union[float, int]`. But in this case, by saying we can take a float, we imply we can take an int.

</details>


### Summary:

Remember, type hints are a way to provide hints to developers and tools about the expected types in your code. They are not enforced by the Python interpreter at runtime but can be checked using tools like mypy.
