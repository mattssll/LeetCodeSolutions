class Solution:
    def findDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                return num
         