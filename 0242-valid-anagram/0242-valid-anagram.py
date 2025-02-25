class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # we get 2 dics, do a count
        # base case is that if length of strings is diff return false
        if len(s)!= len(t):
            return False

        dict_s = {}
        dict_t = {}
        for i in range(len(s)):  # s or t, whatever, same len
            # if non existent gets 0, otherwise get value, add 1
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        
        if dict_s == dict_t:
            return True
        else:
            return False
        