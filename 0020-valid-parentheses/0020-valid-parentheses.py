class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # {(})}
        # when getting closing item, need to check previus by popping
        stack = []
        check = {"}":"{",")":"(", "]":"["}
        openings = ["{", "(", "["]
        closings = ["}", ")", "]"]

        for i in s:
            if i in openings:
                stack.append(i)
                continue
            if i in closings: # i = ")"
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                # now check
                if popped == check[i]:
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False


        