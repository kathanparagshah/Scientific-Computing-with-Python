# Project Portfolio

This repository contains five Python projects demonstrating core programming concepts, object-oriented design, and algorithmic thinking. Each project is self-contained and includes usage examples, implementation details, and the key skills applied.

## Table of Contents

- [Arithmetic Formatter](#arithmetic-formatter)
- [Time Calculator](#time-calculator)
- [Budget App](#budget-app)
- [Polygon Area Calculator](#polygon-area-calculator)
- [Probability Calculator](#probability-calculator)
- [Skills & Technologies](#skills--technologies)

## Arithmetic Formatter

A function `arithmetic_arranger` that takes a list of arithmetic problems (addition and subtraction) and returns them arranged vertically and side-by-side. Optionally displays the answers.

**Features:**
- Validates operators, operand digits, and problem count
- Right-aligns numbers with consistent spacing
- Dynamically generates dashes and optional results

**Usage:**
```python
from arithmetic_formatter import arithmetic_arranger
print(arithmetic_arranger([
    "32 + 698", "3801 - 2", "45 + 43", "123 + 49"
], True))
```

## Time Calculator

A function `add_time` that adds a duration to a 12-hour clock time. It handles day rollovers and optional weekday tracking.

**Features:**
- Parses 12-hour time with AM/PM
- Calculates new time with day count
- Supports specifying the starting weekday
- Formats output with (next day) or (n days later) indicators

**Usage:**
```python
from time_calculator import add_time
print(add_time('11:59 PM', '24:05', 'Wednesday'))
# -> '12:04 AM, Friday (2 days later)'
```

## Budget App

A `Category` class representing budget categories. Supports deposits, withdrawals, transfers, and balance tracking. Also includes a `create_spend_chart` function for visualizing spending.

**Features:**
- `deposit`, `withdraw`, `transfer`, and `check_funds` methods
- Ledger-based transaction recording
- Overridden `__str__` for formatted budget statements
- `create_spend_chart` renders a percentage bar chart

**Usage:**
```python
from budget import Category, create_spend_chart
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))
```

## Polygon Area Calculator

Classes `Rectangle` and `Square` demonstrating inheritance. Calculates area, perimeter, diagonal length, visual representation, and nesting counts.

**Features:**
- `get_area`, `get_perimeter`, and `get_diagonal` methods
- `get_picture` ASCII-art rendering (with size limits)
- `get_amount_inside` for fitting one shape into another
- `Square` subclass synchronizes width/height via `set_side`

**Usage:**
```python
from polygon import Rectangle, Square
rect = Rectangle(10, 5)
print(rect.get_area())  # 50
sq = Square(4)
print(rect.get_amount_inside(sq))  # 6
print(sq.get_picture())
```

## Probability Calculator

A Monte Carlo simulation estimating the probability of drawing specific balls from a hat.

**Components:**
- `Hat` class that stores ball colors and supports random draws without replacement
- `experiment` function running repeated trials to approximate probabilities

**Usage:**
```python
from probability import Hat, experiment
hat = Hat(blue=5, red=4, green=2)
prob = experiment(
    hat=hat,
    expected_balls={'red':1, 'green':2},
    num_balls_drawn=4,
    num_experiments=10000
)
print(f"Estimated Probability: {prob}")
```

## Skills & Technologies

- **Python**: Core language features, functions, and modules
- **Object-Oriented Programming**: Classes, inheritance, encapsulation
- **Data Structures**: Lists, dictionaries, and deep copying
- **Algorithms**: Formatting logic, time arithmetic, simulations
- **Randomness & Statistics**: Monte Carlo methods, probability estimation
- **Formatting**: String manipulation, alignment, ASCII-art charts
- **Testing & Validation**: Edge-case handling and unit-test readiness

Feel free to explore each module folder for detailed code and additional examples!