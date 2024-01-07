### What is a virtual environment?  
A virtual environment in Python is a self-contained directory or folder that allows you to create and manage isolated Python environments for your projects. With environments you can easy manage your dependencies and avoid conflicts with different versions of python.

**Virtual environments are used to:**

- Contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
- Contained in a directory, conventionally either named venv or .venv in the project directory, or under a container directory for lots of virtual environments, such as ~/.virtualenvs.
- Considered disposable – it should be simple to delete and recreate it from scratch. You don’t place any project code in the environment. 
- Not considered as movable or copyable – you just recreate the same environment in the target location. This is also means we don't share them with others, instead we tell them how to make the equivalent environment on their pc. 

Python has several ways to create and manage virtual environments: 

![virtual environments](../assets/day1/virtual_enviroments.png)

**The 4 most well known are shown in the picture above and are:**

- [conda](https://docs.conda.io/projects/conda/en/stable/)
- [Poetry](https://python-poetry.org/)
- [Mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

---

### Some practical considerations
1. Don’t worry too much about which of the above you use, just pick one. 
2. General rule: Each new project gets its own virtual environment
3. When it comes to choosing the version of Python to use, unless you have a specific reason not to, pick the latest stable version (currently 3.11). You can check when you go to install a specific package if it has requirements for a specific Python version. 

For the entirety of this course we'll use [conda](https://docs.conda.io/projects/conda/en/stable/). Conda comes in two versions: Anaconda, and Miniconda. Anaconda has a graphical user interface attached to it, Miniconda is just used through the command line. I prefer Miniconda but either is fine.  

---

### Installing Conda Instructions 
Follow the guides below. 

- [Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)

- [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)

- [MacOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)

**Creating a Virtual Environment with Conda**
```
conda create -n environment_name python=3.11
conda activate environment_name
```

1. rename environment_name to something sensible for the given project. 

2. You'll know you've successfully activated the environment if the environment name is shown in brackets before the terminal. 
![virtual environments](../assets/day1/virtual_enviros_listed.png)

---

### Installing programs 
[Let's first look at an example from a one of Python's major libraries used to make graphs, plotly:](https://github.com/plotly/plotly.py#installation)

Here we see options to use either conda or pip to install the package.  

When it comes to installing multiple programs at once you can simply list them one after the other. 

```
pip install numpy pandas
```

We can also install a list of programs (usually called `requirements.txt`) using either conda or pip:

```
pip install -r requirements.txt
# or 
conda install --file requirements.txt 
```

---

### conda vs pip installing:

[From conda's documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment):
>Issues may arise when using pip and conda together. When combining conda and pip, it is best to use an isolated conda environment. Only after conda has been used to install as many packages as possible should pip be used to install any remaining software. If modifications are needed to the environment, it is best to create a new environment rather than running conda after pip. When appropriate, conda and pip requirements should be stored in text files.

---

### Sharing your environment using Conda:

To share your environment with others or yourself (if for example, you have both a pc and desktop or you want to install something on a computing cluster) you can make a copy of your current environment using: 

```
conda env export > environment.yml
```

This creates a file `environment.yml` which can then be used to create a new environment with the following command:

```
conda env create -f environment.yml
```

Note that you can change the environment name by modifying the first line of the `environment.yml` file. 

[The instructions for this are described in more detail here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment)

---

### Sharing your environment using Pip:

We can do effectively the same thing with pip using the [freeze command](https://pip.pypa.io/en/stable/cli/pip_freeze/)

```
python -m pip freeze > requirements.txt
```

```
# example contents of requirements.txt
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

Now to install the `requirements.txt` file.
```
python -m pip install -r requirements.txt
```

---

### Install Requirements 

Inside a `requirements.txt` file you might see the following symbols associated with the a given Python package (in this case named "SomeProject"). 

```
SomeProject
SomeProject == 1.3
SomeProject >= 1.2, < 2.0
```

These are constraints on the version of the package that can be used. This will be read by the installer. 

---


### What about Containers?
Containers which can be created and run by programs like [Docker](https://docs.docker.com/get-started/overview/) and [Singularity](https://sylabs.io/singularity/) offer a very robust way to create a reproducible environment through creating "containers". For most programming projects involving scientific data analysis, virtual environments should suffice, so these are not covered in this course. If you do plan to learn a tool to run/make Containers, consider that the [university's HPC prefer Singularity over Docker.](https://www.uppmax.uu.se/support/user-guides/singularity-user-guide/)

---

### Extra Reading/Watching:

- [Conda commands cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- [requirements.txt file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
