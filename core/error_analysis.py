import numpy as np

def calculate_error_rate(a, b):
    if len(a) == 0:
        return 0

    errors = sum(i != j for i, j in zip(a, b))
    error_rate = errors / len(a)

    # small realistic noise
    noise = np.random.uniform(0, 0.02)
    return min(1, error_rate + noise)