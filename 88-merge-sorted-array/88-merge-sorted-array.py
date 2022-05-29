class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        # remove exceding items in nums1
        for i in range(len(nums1)):
            if i < m:
                pass
            else:
                nums1.pop(j)
                j -= 1
            j += 1
        # add relevant items from nums1 into nums1
        for z in range(n):
            nums1.append(nums2[z])
        
        # finally just sort the list and it's finished
        nums1.sort()
    