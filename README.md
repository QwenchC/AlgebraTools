# AlgebraTools
The least common factor, the least common multiple and the number of primes in a certain range are solved.

## Project Overview

This project is a toolkit for performing polynomial and numerical computations, including finding the greatest common divisor (GCD) and least common multiple (LCM) of polynomials, calculating the GCD and LCM of multiple numbers, and counting the number of prime numbers less than a given number. Users can select the desired computation tool via an interactive menu, input the relevant data (such as numbers or polynomials), and the program will compute and return the results.

## Features

- **Polynomial GCD**: Compute the greatest common divisor of multiple polynomials.
- **Polynomial LCM**: Compute the least common multiple of two polynomials.
- **Numerical GCD**: Compute the greatest common divisor of multiple numbers.
- **Numerical LCM**: Compute the least common multiple of multiple numbers.
- **Count Primes Less Than a Number**: Count the number of prime numbers less than a given number.

## Project Structure
```
project/
│
├── poly_operations.py # Contains polynomial-related operations
├── number_operations.py # Contains numerical-related operations
├── prime_operations.py # Contains prime number-related operations
├── main.py # Main program for user interaction
└── utils.py # Utility functions
```

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```
   
2. **Install dependencies**:

    The project mainly depends on `numpy`. You can install it with:
    ```bash
    pip install numpy
    ```
   
3. **Usage Guide**:

    Run the main program:
    ```bash
    python main.py
    ```
   
    Select a computation tool: Once the program starts, it will display a menu allowing you to choose the desired tool:

    - 1: Polynomial GCD
    - 2: Polynomial LCM
    - 3: Numerical GCD
    - 4: Numerical LCM
    - 5: Count Primes Less Than a Number

    **Input Data**:
    
    - **Polynomial Input**: Enter the coefficients of the polynomials (from highest to lowest degree, separated by spaces).
    - **Number Input**: Enter multiple numbers (separated by spaces).

    **View Results**: The program will calculate and display the results based on the input data.

## Examples

### Compute the GCD of Multiple Polynomials

- Select option `1`.
- Enter the number of polynomials.
- Input the coefficients of each polynomial, e.g., `1 0 -2` represents $x^2 - 2$.
- View the computed GCD result.

### Compute the LCM of Multiple Numbers

- Select option `4`.
- Enter multiple numbers, e.g., `12 18 24`.
- View the computed LCM result.

## Contribution

Contributions to this project are welcome! You can participate in the following ways:

- **Submit Issues**: If you encounter any issues or have suggestions for improvement, please submit an [issue](https://github.com/yourusername/yourrepository/issues).
- **Submit Pull Requests**: Contributions for new features or bug fixes are welcome. Please ensure your code adheres to the project's coding standards.

---

Thank you for using this project! We hope it proves helpful in your work.
