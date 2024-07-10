class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        
        for val in nums:
            count[val] = 1 + count.get(val,0)
        
        res = []
        for n, c in count.items():
            arr[c].append(n)
        print(arr) #[[], [3], [2], [1], [], [], []]

        for i in range(len(arr) - 1, 0, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res

        

        