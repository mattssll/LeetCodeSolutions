class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)  # Convert to set for O(1) lookups
        max_size = 0
        for num in nums:
            # Only start a sequence if num-1 is NOT in the set
            if num - 1 not in nums:
                current_num = num
                size = 1
                # Expand forward
                # Expand forward
                while current_num + 1 in nums:
                    current_num += 1
                    size += 1

                max_size = max(max_size, size)

        return max_size
