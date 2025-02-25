class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        helper_dict = {}
        # we will do a single pass
        for i, n in enumerate(nums):
            # target = n + result
            needed = target - n
            # in single pass if result is in dict we return,
            # otherwise add to dict
            if needed in helper_dict:
                return [i, helper_dict[needed]]
            else:
                helper_dict[n] = i

