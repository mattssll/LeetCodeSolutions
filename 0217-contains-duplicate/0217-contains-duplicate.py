class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0, len(nums)):
            if i==len(nums)-1:
                return False
            if nums[i]==nums[i+1]:
                return True
        return False
