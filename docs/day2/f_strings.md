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
# awkward because have to take care get the spacing correct.
name = "Alice"
age = 30
message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
```





---

#### f-strings work with expressions

TODO, e.g. can do calculations, index dictionary etc...

---


#### f-string formatting

TODO
format decimals etc...

---

#### f-strings for print debugging.

If you ever do print debugging, it is good to know about the `=` symbol. This will mean both the variable's name and contents are printing to the screen.

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

- what is raw string.
- you can combine a raw and f-string.


---

#### Extra content related to f-strings:

- [Youtube tutorial](https://www.youtube.com/watch?v=Mfmr_Puhtew)
- [RealPython article](https://realpython.com/python-f-strings/)