class Solution(object):
    def rob(self, nums):
        memo = {}

        def rob_helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            result = max(rob_helper(i - 2) + nums[i], rob_helper(i - 1))
            memo[i] = result
            return result

        return rob_helper(len(nums) - 1)