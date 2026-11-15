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






"""
Theory & Code Overview:
This script solves the Fractional Knapsack problem using the Greedy Method, which aims to maximize
total profit within a fixed weight capacity by allowing items to be broken into smaller fractions[cite: 3].
The 'fractional_knapsack' function first sorts the list of (profit, weight) tuples in descending
order based on their profit-to-weight ratio (value density) using a lambda function[cite: 3]. It then
iterates through the sorted items, greedily taking the entirety of each highest-ratio item as long
as the remaining capacity permits[cite: 3]. Once it encounters an item heavier than the remaining capacity,
it takes the exact fraction that fits (profit * capacity / weight), adds that proportional profit to
the total, and terminates the loop[cite: 3]. Because the algorithm is dominated by sorting the items, it runs
in O(n log n) time complexity with O(n) auxiliary space complexity[cite: 3].
"""