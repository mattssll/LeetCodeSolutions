class Solution:
    def isValid(self, s: str) -> bool:
        """
        Opening should be followed by closing (of same item)
        We handle two cases, when it's an opening item, we add to stack
        when it's a closing item, we check the value in the lookup_dict,
        and if it matches, then we remove from stack (cause it's good),
        if not, then we return false and we say it's not valid
        """
        stack = []
        lookup_dict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        for char in s:
            if char in lookup_dict.values():
                stack.append(char)
            elif char in lookup_dict.keys():
                if stack and stack[-1] == lookup_dict[char]:
                    stack.pop()
                else:
                    return False
            
        if stack == []:
            return True
        