class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        left = 0
        right = len(words)-1

        while left <= right:
            tmp = words[left]
            words[left] = words[right]
            words[right] = tmp
            left+=1
            right-=1

        return ' '.join(words)