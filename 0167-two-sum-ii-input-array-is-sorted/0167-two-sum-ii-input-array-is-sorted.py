class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            # Check if the target is found
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            # If the sum is too large, move the right pointer leftward
            elif current_sum > target:
                right -= 1
            # If the sum is too small, move the left pointer rightward
            else:
                left += 1

        # This will never be reached as the problem guarantees exactly one solution
        return []