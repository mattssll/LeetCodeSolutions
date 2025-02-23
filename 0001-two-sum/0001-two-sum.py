class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[v] = i
            # target = a + b; a is v
            # b = target-a
            # if diff is in target then return
            # otherwise we add to hash map
