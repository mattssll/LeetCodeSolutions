class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        track = set()
        for item in nums:
            if item in track:
                return True
            else:
                track.add(item)
        return False
