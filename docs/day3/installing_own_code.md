
Lets say you have a function that you need to use several times throughout your project. This includes in different python files and notebooks. 

```
def my_own_special_function() -> None:
    """Print hello world """
    print("hello world")
```

We could just copy-paste the function into all the different files we need to use, but this probably wont end well, because we will end up with duplicate code and what happens if we need to change it. 

Instead, we can write the function down in one place and install it. 

Then to use it anywhere in our project we can do something like:

```
from my_package.special_functions import my_own_special_function

my_own_special_function()
```

As you can see, now it becomes just like using a function from NumPy or Pandas, and we only have one place where we need to edit the code if we need to (if for example there is a bug or we want to change it's functionality). 

---

### Setting This Up

The first time setting this up can be awkward, but after that it becomes quite straight forward. 

To set this up, we'll need to:

- A folder to store our installable code inside of.  
- An `__init__.py` file. - This makes the directory the file is in be recognized as a module by Python. 
- A `setup.py` file that effectively works as a configuration file. 


**Teacher note:** [Show an example of installable code on the internet](https://github.com/kamerlinlab/KIN)


---

### Folder Structure 

The folder structure we will use is as follows: 

```
├─ src   
│  └─ my_package 
│     ├─ __init__.py
│     └─ ...
├─ tests
│  └─ ...
├─ data
│  └─ ...
├─ modelling 
│  └─ ...
└─ setup.py
```

The file `__init__.py` inside the directory `my_package` makes the .py files inside the directory be recognized as modules by Python. 

The `__init__.py` needs to be there but can be empty.  

Note, there is technically another way to setup your folder structure, but it goes a bit beyond the scope of the session to talk about here. The long story short is that either works for what we are doing here, so I'm only going to show one. [You can read more about it here.](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

---

### The setup.py file

Here is a basic setup.py that we can talk through: 

```
from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "A python package to do something"
LONG_DESCRIPTION = """
A more detailed description of what this package does. 
Can be multiple lines if you like. 
"""

setup(
    name="package_name",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="your name here",
    author_email="your email here if you want",  
    url="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "notebook",
        "scikit-learn",
        "numpy",
        "pandas",
        "plotly",
        "kaleido",
    ],
    extras_require={
        "dev": ["pytest", "black", "setuptools", "twine"],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
```

Note that the setup.py file is stored in the outermost folder of your project directory. This is the standard. 

[You can read more about the setup.py file here.](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)

---

### Installing your code: 

Now with the files and folders needed we can run the following command **after** activating our virtual environment. 

```
# make sure you virtual environment is active
pip install --editable . 
```

- The `.` means in this folder (it will find the `setup.py` file thanks to this). 
- The `--editable` part of the command means if we make changes to our source code (inside the `src` folder)


In some cases, different users of a project might have different dependencies. A common occurrence can be that someone who develops the code will need to install extra programs to help with things like testing or developing the code. This can be specified in the `setup.py` as we saw above:

```
extras_require={
    "dev": ["pytest", "black", "setuptools", "twine"],
```

Here, we are effectively saying someone who develops (dev) this code needs these packages, but someone who just uses this code does not. By default using: 

```
pip install . 
or 
pip install --editable . 
```

will not install these packages. To do this we can run:

```
pip install ".[dev]"
# or 
pip install --editable ".[dev]" 
```

This will install BOTH the dev specific packages and the original set of packages. 

---

### Exercise:

Create a new project folder and add your own module (a python file) with installable code. Validate that you can import and use your code, and that any edits you make are automatically updated in your installation of the code (i.e., you installed the code using the `--editable` flag). 

---

### Further Reading:

- [A complete guide on making code that is available for install by others using pip.](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/) 
- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
