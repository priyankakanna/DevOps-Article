def fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
num_terms = 10  # Number of terms in the Fibonacci series
fib_series = fibonacci(num_terms)
print("Fibonacci Series:")
print(fib_series)