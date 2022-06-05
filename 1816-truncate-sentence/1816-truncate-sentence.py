class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list_of_words = s.split(" ")
        return " ".join(list_of_words[0:k])
        