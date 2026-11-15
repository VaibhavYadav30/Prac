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
