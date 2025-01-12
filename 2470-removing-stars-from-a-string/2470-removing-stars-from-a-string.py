class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for i in s:
            if i=="*":
                result.pop()
            if i!="*":
                result.append(i)
        return ''.join(result)