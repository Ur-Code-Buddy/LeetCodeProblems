class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr1 = set(nums1)
        arr2 = set(nums2)
        res = []
        
        if len(arr1) > len(arr2):
            for i in arr1:
                if i in arr2:
                    res.append(i)
        else:
            for j in arr2:
                if j in arr1:
                    res.append(j)
                    
        return res