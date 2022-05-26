class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        list_size = len(nums)
        
        if nums[0] > target:
            return 0
        
        for i, v in enumerate(nums):
            
            if v == target:
                return i
            elif i+1 == list_size:
                return i + 1
            
            else:
        
                if target < nums[i+1]:
                    return i+1            
                else:
                    continue
                
        return result