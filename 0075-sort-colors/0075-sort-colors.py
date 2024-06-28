class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroPtr,onePtr = 0,0
        twoPtr = len(nums) - 1

        while onePtr <= twoPtr:
            if nums[onePtr] == 0:
                nums[onePtr],nums[zeroPtr] = nums[zeroPtr], nums[onePtr]
                zeroPtr += 1
                onePtr += 1
            elif nums[onePtr] == 1:
                onePtr += 1
            else:
                nums[onePtr],nums[twoPtr] = nums[twoPtr], nums[onePtr]
                twoPtr -= 1

            



        