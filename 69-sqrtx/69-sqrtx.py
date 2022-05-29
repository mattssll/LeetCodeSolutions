class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            result = i * i
            if result == x:
                return i
            elif result > x:
                return i - 1
                        
            
            