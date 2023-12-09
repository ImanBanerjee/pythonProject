# Function to calculate the square of a number
def square(number):
    result = number * number
    return result

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(square(n))):  # Error: Range should be up to the square root of n
        if n % i == 0:
            return False
    return True

# Function to print the Fibonacci sequence up to a given term
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

# Sample usage of the functions
num_to_square = 4
result = square(num_to_square)
print(f"The square of {num_to_square} is: {result}")

num_to_check = 13
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")

fibonacci_sequence = fibonacci(8)
print(f"The first 8 terms of the Fibonacci sequence are: {fibonacci_sequence}")
# Compare this snippet from Boolean_Practice.py:
