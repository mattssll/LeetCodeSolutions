class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        for i,v in enumerate(nums):
            running_sum = v + running_sum
            if i == 0:
                continue
            else:
                nums[i] = running_sum
        return nums
            
            
            
            