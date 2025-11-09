class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n  # Base cases: F(0) = 0, F(1) = 1
        return self.fib(n - 1) + self.fib(n - 2)  # Recursive formula
