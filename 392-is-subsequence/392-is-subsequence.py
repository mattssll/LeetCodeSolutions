class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        p = 0
        for item in t:
            try:
                if s[p] == item:
                    p += 1
            except:
                break
                continue
        if len(s) == p:
            return True
        else:
            return False

            
