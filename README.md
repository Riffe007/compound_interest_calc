# Calculus Toolkit

An advanced toolkit for numerical calculus operations, including derivative computation and function parsing, complemented by an interactive PyQt5 GUI. This repository demonstrates professional code organization, robust error handling, and logging—perfect for showcasing on your resume.

## Features

- **Numerical Derivative Calculation:** Compute the derivative of any single-variable function using a finite difference method.
- **Function Parsing:** Convert string expressions into callable functions using Sympy.
- **Interactive GUI:** A polished PyQt5 interface for real-time derivative computation.
- **Logging & Error Handling:** Comprehensive logging via decorators and robust error handling to facilitate debugging.
- **Unit Testing:** Built-in tests for critical functions ensure reliability and maintainability.

## Repository Structure

- `calculus.py` - Contains the numerical derivative function along with unit tests.
- `parser.py` - Parses mathematical expressions into callable functions.
- `gui.py` - A PyQt5-based graphical user interface for derivative calculation.

## Prerequisites

- Python 3.7+
- [Sympy](https://www.sympy.org/) for symbolic mathematics
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) for the GUI

Install the required packages using pip:

```bash
pip install sympy pyqt5
```
## Usage
Running Unit Tests
Each module contains a built-in unit test that you can run directly. For example:
```bash
python calculus.py
python parser.py
```

## Launching the GUI
To start the PyQt5 GUI, run:
```bash
python gui.py
```

## Code Quality & Design
  - Modular Design: Each component is encapsulated in its own module.
  - Logging Decorators: All key functions are wrapped with logging decorators for traceability.
  - Error Handling: Robust error management gracefully handles unexpected inputs and computation issues.
  - Extensible: The structure allows for the easy addition of more advanced calculus operations.

## Future Enhancements
  - Extend the GUI with additional calculus operations.
  - Integrate advanced plotting features for visualizing functions and their derivatives.
  - Add comprehensive continuous integration and more extensive testing.

## License
This project is licensed under the MIT License.
