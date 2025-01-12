class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()  # Sort the array to make it easier to calculate subsequences
        i = 0
        j = len(nums) - 1
        mod = (10**9)+7
        while i <= j:  # Allow the case where i == j
            if nums[i] + nums[j] <= target:
                # Count all subsequences between nums[i] and nums[j]
                res += 2 ** (j - i)  # (j - i) elements can form subsequences
                i += 1  # Move to the next element from the left
            else:
                j -= 1  # Move to the next element from the right

        return res%mod
        # By using res % mod, you're taking the remainder when dividing the result by a large prime number, mod = 10^9 + 7. 
        # This ensures that the result fits within the bounds of a 32-bit or 64-bit integer.