def knapsack_01(weights, values, capacity):
    """Solves the 0/1 Knapsack problem using Dynamic Programming."""
    n = len(weights)
    
    # Create a DP table initialized with zeros
    # Rows represent items (0 to n), Columns represent capacities (0 to capacity)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Check if the current item's weight can fit into the current capacity
            if weights[i-1] <= w:
                # Max of:
                # 1. Including the item (value of item + remaining capacity value)
                # 2. Excluding the item (value from the previous row at same capacity)
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Item is too heavy; carry forward the value excluding this item
                dp[i][w] = dp[i-1][w]
                
    return dp[n][capacity]


def main():
    print("--- 0/1 Knapsack Solver (Dynamic Programming) ---")
    
    try:
        # 1. Accept item weights and values
        weights_input = input("Enter item weights separated by spaces: ")
        weights = [int(w) for w in weights_input.split()]
        
        values_input = input("Enter item values separated by spaces: ")
        values = [int(v) for v in values_input.split()]
        
        # Validation check for matching item lengths
        if len(weights) != len(values):
            print("Error: The number of weights must match the number of values.")
            return

        # 2. Accept bag capacity
        capacity = int(input("Enter the maximum bag capacity: "))
        
        if capacity < 0:
            print("Error: Capacity cannot be negative.")
            return

        # 3. Calculate using Dynamic Programming
        max_value = knapsack_01(weights, values, capacity)
        
        # 4. Display the maximum obtainable value
        print("\n--- Results ---")
        print(f"Maximum obtainable value: {max_value}")
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")


if _name_ == "_main_":
    main()
