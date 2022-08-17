class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_counter = 0
        counter = 0
        for i, v in enumerate(nums):
            if i==0:
                counter += 1
                max_counter = counter
                continue
            difference_minus_one = v - nums[i-1]
            if difference_minus_one == 0:
                continue
            elif difference_minus_one == 1:
                counter +=1
                if counter > max_counter:
                    max_counter = counter
                continue
            else:
                counter = 1
            
        return max_counter
        