import numpy as np


def log_sum_exp(x: np.ndarray) -> np.ndarray:
    """Compute Log-Sum-Exp stably along the last axis."""

    # Find the maximum value from each row
    x_max = x.max(axis=1)

    # Subtract the row-wise maximum before exponentiation
    # to prevent overflow for very large input values
    x_shifted = x - x_max[:, None]

    # Compute log(sum(exp(x))) using the shifted values
    result = x_max + np.log(
        np.sum(np.exp(x_shifted), axis=1)
    )

    # Return one Log-Sum-Exp value for each row
    return result


# Read a 2D array from user input
# Example: [[2.0, 1.0, 0.1], [0.5, 2.5, 0.3]]
x = np.array(eval(input()))

# Compute and display the Log-Sum-Exp values
print(log_sum_exp(x))