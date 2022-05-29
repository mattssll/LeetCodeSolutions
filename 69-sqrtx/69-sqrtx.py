class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        for i in range(0,x+1): 
            
            result = i * i
            
            if result == x:
                return i
            elif result > x:
                return i - 1
            
            
            