# Fourier Series Drawing Animation

This project is a Python application that provides a visual demonstration of the Fourier series. It takes a user-defined drawing, represented as a series of 2D points, and reconstructs it using a set of rotating vectors, often called epicycles. This creates a beautiful animation where the tip of the final vector traces out the original shape.

This was built to practicalize concepts learned in an Engineering Mathematics course, specifically showing how a complex periodic function (a drawing) can be decomposed into a sum of simple sinusoids.

## How It Works

The core of the project is the Fourier series, which in its complex form can be expressed as:

`f(t) ≈ Σ c_n * e^(2πint)`

The process is broken down into two main parts: analysis and synthesis.

### 1. Analysis (Calculating Coefficients)

The program first analyzes the input drawing to calculate the Fourier coefficients (`c_n`).

*   The input drawing from `vector_img.py` is treated as a path of complex numbers `f(t) = x(t) + iy(t)`.
*   The `get_coef(n)` method in `main.py` calculates the *n*-th coefficient by performing a Discrete Fourier Transform (DFT). This is a numerical approximation of the integral:
    `c_n = ∫[0 to 1] f(t) * e^(-2πint) dt`
*   Each coefficient `c_n` is a complex number representing the amplitude and initial phase of the *n*-th epicycle. The more coefficients calculated, the more accurate the final drawing will be.

### 2. Synthesis (Drawing the Epicycles)

Once the coefficients are known, the program reconstructs the drawing.

*   The `draw(t)` method in `main.py` performs this synthesis.
*   In the main animation loop, for each time `t`, it calculates the state of the epicycle chain using the formula `Σ c_n * e^(2πint)`.
*   Each term `c_n * e^(2πint)` represents a vector that rotates at a frequency of `n` cycles per period.
*   These vectors are drawn chained together, with each vector starting from the tip of the previous one.
*   The path traced by the tip of the final vector in the chain is recorded and drawn to the screen, which visually reconstructs the original shape.

## Project Structure

*   `main.py`: The main application file that runs the Pygame animation. It handles the main loop, performs the Fourier analysis to get the coefficients, and synthesizes the drawing with the epicycles.
*   `complex_num.py`: A helper class `Z` for complex number arithmetic. This was created to provide an intuitive way to handle the mathematical operations (addition, multiplication, polar conversion) required for the Fourier calculations.
*   `vector_img.py`: This file contains the raw data for the drawings. The `pts1` and `pts2` variables are lists of (x, y) coordinates. You can add your own lists of points to draw different shapes.

## How to Run

### Prerequisites

*   Python 3.x
*   Pygame

You can install Pygame using pip:
```sh
pip install pygame
```

### Execution

To run the animation, simply execute the `main.py` file:
```sh
python main.py
```
