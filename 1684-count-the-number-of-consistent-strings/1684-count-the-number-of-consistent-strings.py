class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result_counter = 0
        for item in words:
            wrong = 0
            for word in item:
                if word not in allowed:
                    wrong += 1
            if wrong == 0:
                result_counter += 1
        return result_counter
        