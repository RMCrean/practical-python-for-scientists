

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
You may have been tempted to write `int` or `Union[float, int]`. But in this case, by saying we can take a float we can take an int.  








Any: Represents a variable of any type.
Union: Indicates that a variable can have one of several types.


Remember, type hints are a way to provide hints to developers and tools about the expected types in your code. They are not enforced by the Python interpreter at runtime but can be checked using tools like mypy.


## Comments:
Use comments sparingly, 

## Variable Naming
Variable names should be clear and descriptive 

#### Naming Regular Objects:

#### Naming Classes:
Classes in python are typically named in CamelCase format. 
If you see an object

#### Naming Constants:
Constants are things that don't change from start to finish in your code. When you or someone else uses your code it can be useful to explicity label that these things are constant. In Python we do this by naming the object in ALL_CAPITALS.

In a script, constants should be provided at the top of the file after the imports and before any code:

**Some example constants**
```
PI_2_DECIMAL_PLACES = 3.14
INPUT_FILE_PATH = r"folder1/folder2/file_name.txt"
SCREEN_RESOLUTION = (1280, 720)
```



### f-strings:
Type hints explanation







### Basic script Layout:
show modules loaded, constants, some functions, main logic, if __name___ ... etc.. 