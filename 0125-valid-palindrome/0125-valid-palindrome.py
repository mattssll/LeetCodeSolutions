class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        l=0
        r=len(s)-1
        equal = True
        while l<r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        
        return True
        
        