class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check = {")": "(", "}": "{", "]": "["}  # Closing to opening mapping

        for char in s:
            if char in check:  # If it's a closing bracket
                if not stack or stack.pop() != check[char]:
                    # not stack means if stack is empty # '{}]' or ']'
                    return False
            else:
                stack.append(char)  # It's an opening bracket

        return not stack  # Stack should be empty if valid
