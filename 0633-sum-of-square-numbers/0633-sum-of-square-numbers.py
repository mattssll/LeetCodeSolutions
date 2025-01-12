class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0  # Start from the first element
        # we do c**0.5 because j**2 has to be < c
        # j**2 < c can be written as j < sqrt(c) - thus c**0.5 as our right limit
        j = int((c**0.5)+1)
        while i <= j:
            # Check the sum of squares
            res = (i ** 2) + (j ** 2)
            
            if res == c:
                return True  # If sum of squares equals c, return True
            elif res > c:
                j -= 1  # Sum is too large, move j left to decrease the sum
            else:
                i += 1  # Sum is too small, move i right to increase the sum
        
        return False  # No valid pair found
