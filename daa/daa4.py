# 0/1 Knapsack using Dynamic Programming

def knapsack(capacity, weight, profit, n):
    #2d tabel
    dp = [[0 for x in range(capacity + 1)]
          for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weight[i-1] <= w:
                dp[i][w] = max(
                    profit[i-1] + dp[i-1][w-weight[i-1]],#include items
                    dp[i-1][w]#exclude item
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# Main program
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

n = len(profit)

print("Maximum Profit:", knapsack(capacity, weight, profit, n))



















"""
Theory & Code Overview:
This script solves the 0/1 Knapsack problem using Bottom-Up Dynamic Programming (Tabulation) to
maximize total profit without exceeding a given weight capacity, where each item must either be
taken completely (1) or left behind (0). Because greedy selection fails for indivisible items, the
'knapsack' function constructs a 2D table 'dp' of size (n + 1) x (capacity + 1) to store optimal
subproblem solutions for the first 'i' items at every capacity 'w' from 0 to 'capacity'. Using nested
loops, if the current item's weight fits within 'w' (weight[i-1] <= w), it records the maximum
value between including the item (profit[i-1] + dp[i-1][w - weight[i-1]]) and excluding it
(dp[i-1][w]); otherwise, it carries forward the previous value (dp[i-1][w]). Finally, dp[n][capacity]
returns the overall maximum profit in O(n * capacity) pseudo-polynomial time and O(n * capacity)
space complexity.
"""