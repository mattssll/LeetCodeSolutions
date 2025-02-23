class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i<j:
            t_sum = numbers[i]+numbers[j]
            if t_sum==target:
                return [i+1, j+1]
            elif t_sum>target:
                # decrease our t_sum
                j-=1
            else:
                # increase t_sum
                i+=1
        return