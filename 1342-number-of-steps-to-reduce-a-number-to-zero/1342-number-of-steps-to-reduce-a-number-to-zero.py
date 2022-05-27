class Solution:
    def numberOfSteps(self, num: int) -> int:    
        counter = 0        
        while num != 0: 
            is_even = True if num % 2 == 0 else False   
            if is_even:
                num = num/2
            else:
                num -= 1
            counter += 1
        return counter
        
        
        