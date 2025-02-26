class Solution(object):
    def get_char_frequency(self, word):
        frequency = {
            letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'
        }  # Initialize for 'a' to 'z'
        for letter in word:
            frequency[letter] = frequency.get(letter, 0) + 1
        return str(frequency)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        frequency = {
            letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'
        }  # Initialize for 'a' to 'z'
        res_dict = {}
        for word in strs:
            w_freq = self.get_char_frequency(word)
            if w_freq not in res_dict:
                res_dict[w_freq] = [word]
            else:
                res_dict[w_freq].append(word)
        
        for a_group in res_dict.values():
            res.append(a_group)
        
        return res

        