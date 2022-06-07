class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # using a simple counter, we send the jewels to a list and check for each stone if they are a jewel
        counter = 0
        for stone in stones:
            if stone in list(jewels):
                counter +=1
        counterD = 0
        # using a dict, we build a dict with the stone name as a key and quantity as a value,
        # then for each of the jewels we sum the quantity of the dict for the jewels
        countDict = collections.Counter(stones)
        for j in jewels:
            if countDict[j]:
                counterD += countDict[j]
        return counterD
    
            