class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        for c, n in counts.items():
            freq[n].append(c)

        counts = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                counts.append(n)
                if len(counts) == k:
                    return counts