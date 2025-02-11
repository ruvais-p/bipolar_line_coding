# Line Coding Visualization

## Overview
This project provides a Python-based visualization tool for various line coding techniques, including:

- **AMI (Alternate Mark Inversion)**
- **Pseudo-Ternary Encoding**
- **B8ZS (Bipolar with 8-Zero Substitution)**
- **HDB3 (High-Density Bipolar-3 Encoding)**

The program allows users to input a binary sequence, encodes it using the above techniques, and plots the results using Matplotlib.

## Features
- Accepts user input for binary sequences.
- Implements four different line coding schemes.
- Uses Matplotlib to visualize the encoded signals.
- Clearly marks binary input and respective encoded values.

## Installation
To run this project, ensure you have Python installed. You also need the following dependencies:

```sh
pip install numpy matplotlib
```

## Usage
Run the script using:

```sh
python line_coding.py
```

Then, input a binary sequence when prompted, and the program will generate visual plots of different encoding techniques.

## Encoding Techniques
- **AMI (Alternate Mark Inversion)**: Nonzero pulses alternate in polarity.
- **Pseudo-Ternary**: Similar to AMI, but applies inversion on zeros instead of ones.
- **B8ZS (Bipolar 8-Zero Substitution)**: Replaces long sequences of zeros with a specific pattern to maintain synchronization.
- **HDB3 (High-Density Bipolar 3-Zeros)**: Similar to B8ZS but modifies zero sequences based on previous pulses to maintain DC balance.

## Example Output
When entering the sequence `1010000000`, the program generates step plots for each encoding method, showing their respective signal levels.

## Author
ruvais-p

