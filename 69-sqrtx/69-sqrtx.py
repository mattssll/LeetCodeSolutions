class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x==1:
            return 1
        
        
        for i in range(1,x+1): 
            
            result = i * i
            
            if result == x:
                return i
            elif result > x:
                return i - 1
            
            
            