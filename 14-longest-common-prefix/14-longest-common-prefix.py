class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_smallest_string = len(min(strs, key=len))
        number_of_words = len(strs)
        same_prefix = True
        same_prefix_words = ""
        if strs == [""]:
            return ""
        elif number_of_words == 1:
            return strs[0][0]
        
        for i in range(len_smallest_string):
            
            for j in range(number_of_words):

                if j+1 == number_of_words:
                    break
                elif strs[j][i] == strs[j+1][i]:
                    same_prefix = True
                elif strs[j][i] != strs[j+1][i]:
                    same_prefix = False
                    break
                # print(f"comparing {strs[j][i]} with {strs[j+1][i]}")
            if not same_prefix:
                break
            elif same_prefix:
                same_prefix_words = same_prefix_words + strs[0][i]
            # print("going for another round")
        
        return same_prefix_words
            
            