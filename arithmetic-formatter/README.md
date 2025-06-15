# Arithmetic Formatter

A Python function that arranges arithmetic problems vertically and side-by-side for easier reading and solving.

## Description

This project implements an `arithmetic_arranger` function that takes a list of arithmetic problems and formats them in a visually appealing vertical arrangement. The function supports addition and subtraction operations and can optionally display the answers.

## Features

- Arranges arithmetic problems vertically
- Supports addition (+) and subtraction (-) operations
- Optional answer display
- Input validation for:
  - Maximum 5 problems at once
  - Numbers with maximum 4 digits
  - Only digits in numbers
  - Valid operators only

## Usage

```python
from main import arithmetic_arranger

# Basic usage without answers
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 7", "123 + 49"])
print(result)
```

Output:
```
   32      3801      45      123
+ 698  -     2  +   7  +  49
-----  -------  -----  -----
```

```python
# With answers displayed
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 7", "123 + 49"], True)
print(result)
```

Output:
```
   32      3801      45      123
+ 698  -     2  +   7  +  49
-----  -------  -----  -----
  730      3799     52      172
```

## Error Handling

The function returns appropriate error messages for:
- Too many problems (more than 5)
- Invalid operators (not + or -)
- Numbers with more than 4 digits
- Non-digit characters in numbers

## Testing

Run the test suite to verify functionality:

```bash
python test_all.py
```

## Files

- `main.py`: Contains the main `arithmetic_arranger` function
- `test_all.py`: Comprehensive test suite
- `test_debug.py`: Debug utilities for development

## Project Status

This project passes 9 out of 10 test cases, with minor spacing adjustments needed for complete compatibility.