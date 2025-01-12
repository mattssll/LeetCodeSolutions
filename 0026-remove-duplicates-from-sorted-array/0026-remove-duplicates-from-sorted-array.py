class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            # i is used to iterate
            # j is used for the replacements,
            # then array is erased after j -> [:j]
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return len(nums[:j])
