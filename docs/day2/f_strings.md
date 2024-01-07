In Python, an f-string, or formatted string literal, is a way to embed expressions inside strings by using curly braces `{}`. F-strings were introduced in Python 3.6 and are considered the best practice way to format a string.

To create an f-string, you prefix the string with the letter 'f' or 'F' and then include expressions inside curly braces. The expressions inside the curly braces are evaluated at runtime and their values are inserted into the string.

**Here's a simple example:**

```
name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)
```

**This will output:**

```
Hello, my name is Alice and I am 30 years old.
```

Note that f-strings work with both single (`"` or `'`) and triple (`"""` or `'''`) quotes meaning you can also write multi-line statements with ease.

---

#### Why Use an F-string?

There are many ways to format strings, but f-strings are generally considered the best/most readable way. Compare the f-string we wrote above to the following approaches:

**1. Using % Formatting:**
```
# awkward especially when you have many parameters.
name = "Alice"
age = 30
message = "Hello, my name is %s and I am %d years old." % (name, age)
```

**2. Using Concatenation:**
```
# awkward because have to take care to get the spacing correct.
name = "Alice"
age = 30
message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
```


---

#### f-strings can directly evaluate expressions and run functions 

An f-string can directly evaluate expressions and run functions.  


For example, below the expression `a + b` is determined inside the expression: 
```
a = 5
b = 7
result = f'The sum of {a} and {b} is {a + b}'
```

In the example below, we call the function `square` inside the function. 
```
def square(x):
    return x ** 2

num = 4
result = f'The square of {num} is {square(num)}'
```

---

#### f-string formatting

You can also format the presentation of numerical values, such as specifying the number of decimal places for a floating-point number.

Here are some examples: 

```
# control decimal places
pi = 3.141592653589793
print(f"The value of pi is approximately {pi:.2f}.")
# output: The value of pi is approximately 3.14.
```

```
# use scientific notation
large_number = 1000000
print(f"The number in scientific notation: {large_number:.2e}.")
# output: "The number in scientific notation: 1.00e+06."
```

```
# add commas between each 1000
population = 1000000
print(f"The formatted population is: {population:,}.")
# output: The formatted population is: 1,000,000.
```

```
# convert between decimal to percentage
success_rate = 0.85
print(f"The success rate as a percentage: {success_rate:.1%}.")
# output: The success rate as a percentage: 85.0%.
```

---

#### f-strings for print debugging.

If you ever do print debugging, it is good to know about the `=` symbol. This will mean both the variable's name and contents will be printed to the screen.

**For example:**

```
student = "Tim"
classes = ["chemistry", "history", "french"]
grades = [90, 85, 92]

# Print debugging using f-strings with variable names
print(f"{student=}")
print(f"{classes=}")
print(f"{grades=}")
```

**This will output:**

```
student='Tim'
classes=['chemistry', 'history', 'french']
grades=[90, 85, 92]
```

Essentially, by using {variable_name=}, you not only print the value of the variable but also its name. This can be useful when you have many variables and want to quickly identify which variable is associated with each value.

---

#### Bonus - raw strings

In Python, a raw string is a string prefixed with an `r` or `R` (doesn't make any difference which you use). Raw strings are used to treat backslashes `(\)` as literal characters, [rather than as escape characters](https://www.guru99.com/python-escape-characters.html). This can be particularly useful in scenarios where you want to work with regular expressions, file paths, or any other strings containing backslashes without having to escape them.

Raw strings come in handy when for example working with windows file paths:

```
file_path = r"C:\Users\Username\Documents\example.txt"
print(file_path)
```

Meaning you don't need to escape all of the backslashes `(\)` in the file path. 

Another place they can come in handy is when working with regular expressions, which will be covered in more detail tomorrow: 
```
import re
pattern = r"\d+"
text = "There are 42 apples and 18 oranges."
result = re.findall(pattern, text)
print(result)  # Output: ['42', '18']
```
In the example above, the regex pattern `r"\d+"` is a raw string, and is used to extract all the digits from the text. 


Finally, note that you can combine a raw and f-string together (the ordering of the `r` and `f` does not matter in the example below)

```
files = ["example_1.txt", "example_2.txt", "example_3.txt"]

for file in files:
    file_path = rf"C:\Users\Username\Documents\{file}"
    print(file_path)
```

This would output the following: 
```
C:\Users\Username\Documents\example_1.txt
C:\Users\Username\Documents\example_2.txt
C:\Users\Username\Documents\example_3.txt
```

---

#### Extra content related to f-strings:

- [Youtube tutorial](https://www.youtube.com/watch?v=Mfmr_Puhtew)
- [RealPython article](https://realpython.com/python-f-strings/)