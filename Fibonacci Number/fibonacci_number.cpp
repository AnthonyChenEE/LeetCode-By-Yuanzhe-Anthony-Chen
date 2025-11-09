class Solution {
public:
    int fib(int n) {
        if (n <= 1) return n;      // Base cases: F(0) = 0, F(1) = 1
        return fib(n - 1) + fib(n - 2);  // Recursive Formula
    }
};
