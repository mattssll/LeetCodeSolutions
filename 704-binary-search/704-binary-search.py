import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            
            midpoint = math.floor((begin + end) / 2)
            
            if nums[midpoint] > target:
                end = midpoint - 1  
            elif nums[midpoint] < target:
                begin = midpoint + 1
            else:  # nums[midpoint] == target
                return midpoint
        
        return -1 # if not found