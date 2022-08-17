class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n1 in enumerate(numbers):
            if numbers[i-1] == numbers[i]:
                continue
            for j,n2 in enumerate(numbers):
                if i==j:
                    continue
                if n1+n2==target:
                    return [i+1,j+1]
