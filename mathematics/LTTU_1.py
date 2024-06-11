import numpy as np

def gradient_method_quadratic(A, b, x0, epsilon):
    """
    Gradient method for minimizing the quadratic function f(x) = x.T @ A @ x + 2 * b.T @ x.
    
    Parameters:
    A (numpy.ndarray): The positive definite matrix associated with the objective function.
    b (numpy.ndarray): A column vector associated with the linear part of the objective function.
    x0 (numpy.ndarray): Starting point of the method.
    epsilon (float): Tolerance parameter for the stopping rule.
    
    Returns:
    x (numpy.ndarray): An optimal solution (up to a tolerance) of min(x.T @ A @ x + 2 * b.T @ x).
    fun_val (float): The optimal function value up to a tolerance.
    """
    
    x = x0
    iter_count = 0
    grad = 2 * (A @ x + b)
    
    while np.linalg.norm(grad) > epsilon:
        iter_count += 1
        t = np.linalg.norm(grad)**2 / (2 * grad.T @ A @ grad)
        x = x - t * grad
        grad = 2 * (A @ x + b)
        fun_val = x.T @ A @ x + 2 * b.T @ x
        
        # Print the iteration number, gradient norm, and function value
        print(f'iter_number = {iter_count:3d} norm_grad = {np.linalg.norm(grad):.6f} fun_val = {fun_val:.6f}')
    
    return x, fun_val

# Define matrix A and vector b
A = np.array([[1, 0], [0, 2]])
b = np.array([0, 0])
x0 = np.array([2.0, 1.0])  # Initial point
epsilon = 1e-6             # Tolerance parameter for stopping

# Call the gradient_method_quadratic function
x, fun_val = gradient_method_quadratic(A, b, x0, epsilon)

# Print the results
print("Optimal solution:", x)
print("Optimal function value:", fun_val)
