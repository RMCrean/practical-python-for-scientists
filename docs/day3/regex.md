
Regular expressions are a powerful tool for matching patterns in text. To use regular expressions in Python, you can use the re module. The syntax for using regular expressions is:



```
import re

# Match the pattern "foo"
match = re.match("foo", "foobar")

if match:
  print("The string contains the pattern 'foo'")
else:
  print("The string does not contain the pattern 'foo'")

```

re is the module that contains the regular expression functions
match() is the function that matches a regular expression against a string
r"foo" is the regular expression pattern to match
match is the object that contains the results of the match
if match: is the conditional statement that is executed if the match is successful
print("The string contains the pattern 'foo'") is the code that is executed if the match is successful
else: is the else clause that is executed if the match is not successful
print("The string does not contain the pattern 'foo'") is the code that is executed if the match is not successful


### Formatting Regular Expressions



### Handling edge cases 
example edge cases and how to write expression for them. 


### Tips applying regular expressions
- using raw strings where needed. 
- providing several examples where it works and where it doesn't work. 



### Additional Resources:
- [regex tutorial](https://realpython.com/regex-python/)
