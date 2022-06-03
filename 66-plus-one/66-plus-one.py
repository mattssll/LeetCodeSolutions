class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        We use j as a pointer starting from the last index of array, decrementing it by 1 per iteration
        We use a while loop that runs while j is smaller or equal than 0, then
        We always increment by one the latest index of array, and finally we handle 3 cases:
            a) latest digit when added by 1 is ten, and j is not in first position of array (first if):
                in this case we set digits[j] to 0 and decrement j, so while loop continues
            b) latest digit when added by 1 is ten and j is in first position of array (elif):
                in this case we set digits[j] to 0 and add 1 to the first index of array, and return the array
            c) latest digit when added by 1 is not ten, so we simply return the array
        """
        j = len(digits) - 1
        
        while j>= 0:
            digits[j] = digits[j] + 1
            if digits[j] == 10 and j!= 0:
                digits[j] = 0
                j = j-1
            elif digits[j] == 10 and j == 0:
                digits[j] = 0
                digits.insert(0,1)
                return digits
            else:
                return digits
                