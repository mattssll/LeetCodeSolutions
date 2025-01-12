class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        bigger_word = word1 if len(word1)>=len(word2) else word2
        new_word = ''
        for i in range(0, len(bigger_word)):
            if i<len(word1):
                new_word += word1[i]
            if i<len(word2):
                new_word += word2[i]
        return new_word
        