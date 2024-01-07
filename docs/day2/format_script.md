In this section, we will look at to how format a simple Python script. We can talk through the different parts of this script together.

### Basic script Layout:


Below is a basic script to demonstrate some good practices when writing scripts. 

```

"""
Docstring describing what this file does and any key bits of info
someone reading this should know. 
"""

# Standard library imports
import sys
from datetime import datetime

# Third-party library imports
import numpy as np

# Constants
INPUT_FILE = r"some_foler/input.csv"
OUTPUT_FILE = r"some_foler/output.csv"
MULTIPLICATION_FACTOR = 2


# Helper function 
def process_data(input_data: np.ndarray, multiply_by: float) -> np.ndarray:
    """
    Process the input data.

    Parameters
    ----------
    input_data: np.ndarray, 
    
    multiply_by: float
        Amount to multiply each value inside data by. 

    Returns
    ----------
    np.ndarray: The processed data.
    """
    processed_data = input_data * multiply_by
    return processed_data

def main():
    """
    Main function of the script.
    Where all the different parts of the code come together. 
    """
    input_data = np.genfromtxt(INPUT_FILE, delimiter=",", skip_header=1)
    
    processed_data = process_data(input_data, multiply_by=MULTIPLICATION_FACTOR)
    
    np.savetxt(
        fname=OUTPUT_FILE,
        X=processed_data,
        delimiter=","
    )


if __name__ == "__main__":
    main()
```


#### In the above script we used the following good practices:

- **Localizing Imports:** Import statements are placed at the beginning of the script, separating standard library imports from third-party library imports. This follows the recommended practice of organizing imports. Imports are not placed throughout the script either. 

- **Descriptive Constants:** Descriptive constants (DATA_FILE, OUTPUT_FILE, MULTIPLICATION_FACTOR) are used to represent values that might be reused or modified in the script. 

- **Helper Functions:** The process_data helper function helps to encapsulate specific functionalities, promoting modularity and readability.

- **Documentation and Type Hints:** The module and functions used are documented and type hints are provided. 

- **`If __name__ == "__main__": Block:`** The script includes an `if __name__ == "__main__":` block to ensure that the main function is executed only when the script is run directly, not when it's imported as a module.

---

### Two things to avoid in your scripts:


#### 1. Using "import *"

```
from somepackage import *
from numpy import *
```

This causes two main issues:

- Namespace Cluttering: All names from the module are brought into the current namespace, leading to namespace cluttering, making it unclear which names come from the imported module. Consider that python has a built in `add` function and so does NumPy, so it will not be clear which one you are calling when you write `add`.

- Readability: Explicitly importing only the names you need makes the code more readable. Readers can easily identify where each function or class comes from without having to go back up to the top

**Do instead:** 

```
import somepackage
import numpy as np
```

Note as well that if you only need to use a few things from a package (e.g. `sklearn`) it can also make sense to just import the objects you need directly, for example:

```
import numpy as np
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.compose import ColumnTransformer
```

#### 2. Hardcoding file paths

Instead of hardcoding file paths, use relative paths or configuration files to specify file locations. This improves code portability (usability by others/yourself on another platform). If you need to add file paths to your script consider adding them as constants towards the top of the file, do not bury them somewhere inside the script.




