class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 0
        while i <= x: 
            
            result = i * i
            
            if result == x:
                return i
            elif result > x:
                return i - 1
            i += 1
            
            
            