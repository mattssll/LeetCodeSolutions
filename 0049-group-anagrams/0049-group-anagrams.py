class Solution:
    # The idea is sorting the dict keys and then handling presence (add [word]) and absence (append to value)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        # Iterate through each word in the input list
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in res_dict.keys():
                res_dict[sorted_word] = [word]
            # Generate a frequency dictionary for the word
            else:
                res_dict[sorted_word].append(word)
        return list(res_dict.values())
