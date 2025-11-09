class Solution {
public:
    int fib(int n) {
        if (n <= 1) return n;      // 基本情况：F(0)=0, F(1)=1
        return fib(n - 1) + fib(n - 2);  // 递归公式
    }
};
