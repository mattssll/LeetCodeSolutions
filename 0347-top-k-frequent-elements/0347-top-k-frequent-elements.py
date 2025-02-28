class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        count_dict = {}  # Dictionary to store the frequency of each number
        freq = [[] for _ in range(size + 1)]  # List of lists for bucket sorting
        
        # Count occurrences of each number
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        # Group numbers by their frequency
        for num, count in count_dict.items():
            freq[count].append(num)
        
        # Collect the top k frequent elements
        results = []
        for i in range(size, 0, -1):  # Start from the highest frequency
            for num in freq[i]:
                results.append(num)
                if len(results) == k:  # Stop when we have k elements
                    return results
