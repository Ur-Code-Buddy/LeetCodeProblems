class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is larger than the length of nums

        # Reverse the entire list
        nums.reverse()

        print(nums[:k])
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        print(nums)

        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
