class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(l for l in s if l.isalnum())
        print(s)
        l = 0
        r = len(s)-1
        res = False
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
