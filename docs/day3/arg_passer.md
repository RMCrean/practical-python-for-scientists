
Perhaps you need to regularly process some data obtained from an instrument. The data file output from the instrument is always the same except for the file name and few parameters. You have written a python script to process the data, but with every new experiment you have to go inside the script and update the adjustable parameters. There is another option which is the [argparse module](https://docs.python.org/3/library/argparse.html).

### What is the argparse module:
The argparse module in Python is a standard library module that provides a convenient way to parse command-line arguments. It's particularly useful for creating command-line interfaces (CLIs) for your Python scripts or programs. 

Here are some reasons why someone might want to use the argparse module:

1. User-Friendly Command-Line Interface. It automatically generates help messages. This can be accessed by users typing: `python [script_name.py] --help`. 

2. Argument Parsing: You can specify the arguments (parameters), their types, and whether they are optional or required. argparse handles the conversion of these command-line arguments into Python objects.

3. Default Values: You can set default values for your command-line arguments.

4. Error Handling: argparse provides built-in error handling and will print helpful error messages if users provide incorrect or incomplete command-line input.


### Basic example of python script using argparse
```
import argparse

def main():
    parser = argparse.ArgumentParser(description='A simple script with command-line arguments.')

    parser.add_argument('--input', type=str, help='Input file path', required=True)
    parser.add_argument('--output', type=str, help='Output file path', default='output.txt')

    args = parser.parse_args()

    print(f'Input file: {args.input}')
    print(f'Output file: {args.output}')

if __name__ == '__main__':
    main()
```

This script can then be run with:
`python [script_name.py] --input input_file.txt --output output_file.txt`


In this example, the script takes two command-line arguments (--input, and --output). The argparse module is used to define these arguments, set their types and default values, and then parse the command-line input.

As shown in the script, we can access the value of each arguement using `args.input` or `args.output` within our script.


### Practice using argparser:
Build some simple python scripts that make use of Argparser. 

**1. Calculator:**
- Create a simple calculator script that takes two numbers and can perform the 4 basic arithmetic operations:
(addition, subtraction, multiplication, and division). 
- The script should accept command-line arguments for the operation and the two numbers.

**2. Word Counter:**
- Build a script that counts the number of words in a given text file. 
- Allow the user to specify the file path as a command-line argument.

**3. Temperature Converter:**
- Create a script that converts temperatures between Celsius and Fahrenheit. 
- Let the user specify the temperature value and the unit (Celsius or Fahrenheit) as command-line arguments.




### Extra Reading:
- [Detailed Tutorial on Argparser](https://realpython.com/command-line-interfaces-python-argparse/). 