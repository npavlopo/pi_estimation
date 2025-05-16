import numpy as np
import random

def throw_darts(num_darts):
    in_circle = 0
    for _ in range(num_darts):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            in_circle += 1
    return 4 * in_circle / num_darts

def estimate_pi(num_darts, num_trials):
    estimates = []
    for _ in range(num_trials):
        pi_guess = throw_darts(num_darts)
        estimates.append(pi_guess)
    sigma = np.std(estimates)
    average_estimate = sum(estimates) / len(estimates)
    print("Estimate:", average_estimate, ", Standard Deviation:", sigma, ", Darts:", num_darts)
    return average_estimate, sigma

def calculate_pi(precision, num_trials):
    num_darts = 100
    sigma = precision
    while sigma * 1.96 > precision:
        average_estimate, sigma = estimate_pi(num_darts, num_trials)
        num_darts *= 10
    return average_estimate

# Example run
calculate_pi(0.01, 10)
