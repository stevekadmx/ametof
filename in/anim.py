import numpy as np

def finite_difference_directional_derivative(f, x, v, h=1e-5):
    """
    Approximates the directional derivative of f at x in the direction of v using finite differences.

    Parameters:
        f  : Function to differentiate.
        x  : Point at which to evaluate the derivative (numpy array).
        v  : Direction in which to take the derivative (numpy array, should be a unit vector).
        h  : Step size for finite differences (default is 1e-5).

    Returns:
        Approximation of the directional derivative.
    """
    # Ensure v is a unit vector
    v = v / np.linalg.norm(v)
    
    # Compute the finite difference
    return (f(x + h * v) - f(x)) / h

# Example usage
def example_function(x):
    return x[0]**2 + x[1]**2

x = np.array([1.0, 2.0])
v = np.array([1.0, 1.0])

directional_derivative = finite_difference_directional_derivative(example_function, x, v)
print("Approximate directional derivative:", directional_derivative)
