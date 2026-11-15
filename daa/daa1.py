# Non-Recursive Method
def iterative(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# Recursive Method
def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)


n = int(input("Enter number of terms: "))

print("Non-Recursive:")
iterative(n)

print("\nRecursive:")
for i in range(n):
    print(recursive(i), end=" ")

# Time Complexity (TC) and Space Complexity (SC)
# 1. Non-Recursive Method (Iterative)
# - TC: \(O(n)\) – The loop runs n times.
# - SC: \(O(1)\) – Uses only a fixed number of variables (a, b, c).
# 2. Recursive Method
# - TC: \(O(2^n)\) – Each function call generates two recursive calls.
# - SC: \(O(n)\) – Maximum recursion stack depth is n.




"""
Theory & Code Overview:
This script demonstrates two distinct algorithmic methods—Iteration and Recursion—to generate
the Fibonacci sequence, a mathematical series defined by the recurrence relation F(n) = F(n-1) + F(n-2)
with base cases F(0) = 0 and F(1) = 1. The iterative(n) function uses a 'for' loop and three
variables (a, b, c) as a sliding window to print the sequence sequentially in a single pass,
achieving optimal linear time complexity O(n) and constant space complexity O(1). Conversely,
the recursive(n) function directly translates the mathematical formula into code by repeatedly
branching into two smaller function calls until reaching the base case (n <= 1), requiring the
driver code to loop 'n' times to print each individual term. While conceptually simple, this
naive recursive approach suffers from exponential time complexity O(2^n) due to redundant
calculations of overlapping subproblems, alongside linear space complexity O(n) from the depth
of the system's call stack.
"""