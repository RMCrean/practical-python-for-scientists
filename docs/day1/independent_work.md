
### Topic 1: Error Types

Python has many types of errors built in, for example a `SyntaxError` would be given by the following code:

```
print("Hello"  # Missing closing bracket
```

A `SyntaxError` occurs when the Python interpreter encounters a syntax that violates its grammar rules.

**Assignment:** Learn about some of the most common types of errors. Knowing the type of the error you've raised refers to will help you know how to fix the error. 

**Bonus Question:** What tools can be used to help you spot and fix errors in your code before you've even run the code?  

---

### Topic 2: Context Managers 

We covered try except in class but another useful tool in Python is context managers.  

The most common place to find a context manager is when reading/writing to files:

```
with open('my_book.txt', 'w') as my_file:
    my_file.write('The first line of my book')
```

**Assingment Questions:** 

1. What is a context manager and how does they work in Python. 
2. Why is the above code considered better than the below version?
3. What are some common use cases for context managers?  

```
my_file = open('my_book.txt', 'w')
my_file.write('The first line of my book')
my_file.close()
```

---

### Topic 3: The Command Line 

If you're not already familiar with working with command lines, it is a really useful skill to have. To name somethings it helps with:

- Running Scripts
- Installing and managing Python packages.
- Working with version control systems (e.g., Git)
- Performing file-related operations, such as copying, moving, or deleting files.
- Connecting to and interacting with computing clusters. 

**Assignment:** Find a tutorial and learn the basics of interacting with a command line. 

[If you're already quite experienced with the command line take a look at this](https://github.com/jlevy/the-art-of-command-line/blob/master/README.md)

