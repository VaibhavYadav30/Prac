# Fractional Knapsack using Greedy Method

def fractional_knapsack(capacity, items):
    # Sort items by profit/weight ratio
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_profit = 0

    for profit, weight in items:
        if capacity >= weight:
            total_profit += profit
            capacity -= weight
        else:
            total_profit += profit * (capacity / weight)
            break

    return total_profit


# Main program
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

max_profit = fractional_knapsack(capacity, items)

print("Maximum Profit:", max_profit)

# Time and Space Complexity
# Complexity	Value	Reason
# Time	O(n log n)	Sorting the items
# Space	O(n)	Sorting may require additional space