class Solution(object):
    def optimized_bucket(self, nums, k):
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
    
    def heap(self, nums, k):
        """
        Finds the top k most frequent elements in the list 'nums' using a min-heap.
        """
        import heapq
        # 1. Generate a dictionary to count the frequency of each number in nums
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1  # Increment count for each occurrence

        # 2. Use a min-heap to keep track of the top k elements
        #    The heap will store tuples in the form (frequency, number)
        heap = []
        for key, count in count_dict.items():  # Iterate through each number and its count
            if len(heap) < k:
                # If the heap has fewer than k elements, just push the current (count, key)
                heapq.heappush(heap, (count, key))  
                # Since Python's heapq is a min-heap, it ensures that the smallest frequency
                # is always at the root of the heap.
            else:
                # If the heap already has k elements, we push the new element and remove the smallest one
                heapq.heappushpop(heap, (count, key))  
                # The heap always maintains exactly k elements, and the element with the smallest frequency
                # (least important) is removed when a new element is added.

        # 3. Extract the elements from the heap (only the numbers, ignoring frequencies)
        return [h[1] for h in heap]  # h[1] corresponds to the number, since heap stores (count, number)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # return self.optimized_bucket(nums, k)
        return self.heap(nums, k)
