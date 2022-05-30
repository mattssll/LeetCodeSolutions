class Solution:
    def fib(self, n: int) -> int:
        # We'll solve this issue with recursion
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
            
        return fibonnaci_fx(n)