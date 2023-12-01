## Type Hints:
Type hints allow you to annotate functions and classes you create to indicate the datatype the arguement accepts. 

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
5 is a type int. 

##### We use



##### Type hints for containers 
Containers include types like: ```list, tuple, set, dict: ```

Depending on how specific we want to be we can specificy the types of the data inside the container:

For example the object ```x = [5, 10, 13, 14]``` is of type: ```list[int]```. Meaning it is a list of integers. We could have also simply defined it is as ```list[int]```. 


### Example type hinting of a function
Both the input parameters and outputs can be 





##### Some useful extra type hints
There are some extra tips on type hints:

**1. Consider the function:**
```
def multiply_two_numbers(number_1, number_2):
    return number_1 * number_2
```
What should the type hints be here? 


```
def multiply_two_numbers(number_1: float, number_2: float) -> float:
    return number_1 * number_2
```

<details>
  <summary>Click to reveal awnser</summary>
  You may have been tempted to write `int` or `Union[float, int]`. But in this case, by saying we can take a float, we imply we can take an int. 

</details>

 








Any: Represents a variable of any type.
Union: Indicates that a variable can have one of several types.


Remember, type hints are a way to provide hints to developers and tools about the expected types in your code. They are not enforced by the Python interpreter at runtime but can be checked using tools like mypy.


## Comments:
Use comments sparingly, 


 



### f-strings:








### Basic script Layout:
show modules loaded, constants, some functions, main logic, if __name___ ... etc.. 