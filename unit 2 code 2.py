def fibonacci_tabulation(n):
    # Handle base cases for negative input or zero
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the table (array) with base values
    # dp[0] is the 1st Fibonacci number, dp[1] is the 2nd
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    
    # Iteratively build the solution from the bottom up
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp

# Main program execution
try:
    # Accept N from the user
    num_terms = int(input("Enter the number of Fibonacci terms (N): "))
    
    # Generate the sequence
    sequence = fibonacci_tabulation(num_terms)
    
    # Display the final Fibonacci sequence
    if sequence:
        print(f"The first {num_terms} Fibonacci numbers are:")
        print(sequence)
    else:
        print("Please enter a positive integer greater than 0.")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
