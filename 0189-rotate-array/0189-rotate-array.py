class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []
        n = len(nums)
        k = k % n
        nums.reverse()

        for i in range(k):
            temp.append(nums[i])

        for i in range(k, n ):
            nums[i - k] = nums[i]

        for i in range(k):
            nums[n - k + i] = temp[i]

        nums.reverse()

        print(nums)
