# Monte Carlo Estimation of Pi

This Python project estimates the value of π (pi) using a Monte Carlo simulation. It randomly generates points within a unit square and calculates the proportion that falls within a quarter circle to approximate the value of π.

## Overview

The Monte Carlo method is a probabilistic technique that uses random sampling to obtain numerical results. In this implementation, random (x, y) coordinates are generated, and the proportion of points that fall inside a quarter circle is used to estimate the value of π. The simulation is repeated multiple times to increase accuracy and calculate the standard deviation of the estimates.

## Features

- Estimates the value of π using Monte Carlo simulation
- Runs multiple trials to compute an average value
- Automatically increases the number of samples until a desired precision is achieved
- Prints the current estimate, standard deviation, and number of samples used

## Requirements

- Python 3.x
- NumPy

Install the required dependency with:

```bash
pip install numpy
