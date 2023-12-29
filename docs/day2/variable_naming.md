Variable names should be clear and descriptive. With rare exceptions you should avoid using one or few letter words to describe code. Both others and future you will be grateful if you name your variables clearly.

Different objects in Python have different naming conventions. These naming convetions help us directly understand what the object is when we look at it, making the code more readable.

**Note:** You don't have to follow naming conventions, it's just strongly recommeneded.


### Naming Variables:
Variables are named in all lower case format, with an underscore between each word.

1 letter variable names are generally ill-advised except for certain exceptions. Exceptions include for example "i and j" (math notation), x, y, z (coordinates) and i (when used for keeping track of the index).


### Group exercise, rank the variable name quality
Take a few minutes to rank each of the variable names below into on the following categories: "good", "okay" and "bad".Make sure you can justify why.

**Variable names to rank:**
```
var = True
my_dict = {"registration plate": "KA50 LAQ", "car insurance number": 82192323, "model": "ford_escort"}
a = 2
fruit_list = ["apple", "banana", "cherry"]
my_list = ["apple", "banana", "cherry"]
is_active = False
temperature_celsius = 25.5
```


### Naming Functions:
Like variables, functions are named in all lower case format, with an underscore between each word.

**Some example function names**
```
def bake_bread(ingreidants):
    ...
def print_hello_world():
    ...
def combine_2_dfs(df1, df2, combine_approach):
    ...
```
Note that in the third example, df (short for DataFrame) was used, its okay to use things like this as long as you and others who'll need to use the code understand these acryonnmus. Another examples would be `number` being replaced by `numb` or `num`.

#### Naming Classes:
Classes in python are typically named in CamelCase format.
If you see an object in CamelCase format, chances are that it is a class.

**Some example class**
```
class FileReader:
    ...
class Person:
    ...
class WeatherReport:
    ...
```


#### Naming Constants:
Constants are things that don't change from start to finish in your code. When you or someone else uses your code it can be useful to explicity label that these things are constant. In Python we do this by naming the object in ALL_CAPITALS.

In a script, constants should be provided at the top of the file after the imports and before any code:

**Some example constants**
```
PI_2_DECIMAL_PLACES = 3.14
INPUT_FILE_PATH = r"folder1/folder2/file_name.txt"
SCREEN_RESOLUTION = (1280, 720)
```


### Some extra tips on Constants.

In the above example `SCREEN_RESOLUTION` was defined as a tuple and not a list. Have a think about why that might be the right choice in this case?

<details>
  <summary>Click to reveal awnser</summary>

  Tuples are immutable, meaning their elements cannot be changed or modified after creation. List are mutable on the other hand.
  Once you define a tuple, its elements remain constant. This immutability helps ensure they wont accidently be altered.

</details>
