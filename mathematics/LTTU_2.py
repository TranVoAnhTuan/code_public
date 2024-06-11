import numpy as np

# Define the objective function f(x) = x^T A x
def f(x, A):
    return (x.T @ A @ x).item()

# Define the gradient of the objective function g(x) = 2 A x
def g(x, A):
    return 2 * A @ x

# Gradient method with backtracking stepsize rule
def gradient_method_backtracking(f, g, x0, A, s, alpha, beta, epsilon):
    """
    Gradient method with backtracking step size rule.
    
    Parameters:
    f (function): Objective function.
    g (function): Gradient of the objective function.
    x0 (numpy.ndarray): Initial point.
    A (numpy.ndarray): Matrix A.
    s (float): Initial choice of step size.
    alpha (float): Tolerance parameter for the step size selection.
    beta (float): The constant by which the step size is multiplied at each backtracking step (0 < beta < 1).
    epsilon (float): Tolerance parameter for the stopping rule.
    
    Returns:
    x (numpy.ndarray): Optimal solution (up to a tolerance) of min f(x).
    fun_val (float): Optimal function value.
    """
    
    x = x0
    grad = g(x, A)
    fun_val = f(x, A)
    iter_count = 0
    
    while np.linalg.norm(grad) > epsilon:
        iter_count += 1
        t = s
        
        # Backtracking line search
        while f(x - t * grad, A) > fun_val - alpha * t * np.linalg.norm(grad)**2:
            t *= beta
        
        # Update the solution x
        x = x - t * grad
        
        # Recompute the function value and the gradient
        fun_val = f(x, A)
        grad = g(x, A)
        
        # Print the iteration number, gradient norm, and function value
        print(f'iter_number = {iter_count:3d} norm_grad = {np.linalg.norm(grad):.6f} fun_val = {fun_val:.6f}')
    
    return x, fun_val

# Set the initial parameters
x0 = np.array([0.01,1])  # Initial point (column vector)
A = np.array([[1, 0], [0, 0.01]])  # Matrix A
s = 0.5                      # Initial step size
alpha = 0.1               # Tolerance parameter for the step size selection
beta = 0.5                 # Backtracking constant (0 < beta < 1)
epsilon = 1e-6             # Tolerance parameter for stopping

# Call the gradient_method_backtracking function
x, fun_val = gradient_method_backtracking(f, g, x0, A, s, alpha, beta, epsilon)

# Print the results
print("Optimal solution:", x)
print("Optimal function value:", fun_val)
