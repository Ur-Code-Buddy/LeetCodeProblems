class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        arr = [[] for i in range(1 + len(nums))]

        for val in nums:
            count[val] = count.get(val,0) + 1 #> {1:3, 2:2, 3:1}
        
        res = []
        for n, c in count.items():
            arr[c].append(n)
        
        for i in range(len(arr) - 1, 0 , -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res

        
