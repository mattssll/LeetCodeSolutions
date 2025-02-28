class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # first solution can be used a hashmap,
        # second a heapify
        # better one is a variation of bucket sort
        # 1. we add the num in the index of the count:
        # if number 3 appears 3 times, we add it to index 3
        size = len(nums)
        count_dict = {}
        # should go from 1 to number of elements array (max count n can appear)
        freq = [[] for i in range(size+1)]
        
        # we need a dict with the count of each of the numbers
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1
        
        # now we assign them numbers to the freq
        # if 1 -> 3 (1 appear 3 times) then we add to index 3
        # if n has count(i) -> then we add n to index(i)
        for n, count in count_dict.items():
            freq[count].append(n)        
        print(freq)

        # if we have k = 2 we need to return 2 most frequent
        results = []
        for i in range(len(freq)-1, 0, -1):  # len(freq)-1 because we want to start from latest index
            for number in freq[i]:
                results.append(number)
                if len(results)==k:
                    return results


        