class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myDict = {}
        pairs = 0
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                pairs += myDict[num]
                myDict[num]+=1
        return pairs