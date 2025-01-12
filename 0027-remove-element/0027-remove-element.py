class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0

        for i in range(len(nums)):
            # [1, 2, 1, 1, 1, 3]
            # remove 1
            # 1st iteration, remove 1 ,don't move right pointer
            # 2nd iteration, move to right pointer, move right pointer
            if nums[i] == val:
                continue
            else:
                nums[j] = nums[i]
                j+=1
        return j
        