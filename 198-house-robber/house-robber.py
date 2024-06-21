class Solution(object):
    def rob(self, nums):
        memo = {}

        def _rob(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            result = max(_rob(i - 2) + nums[i], _rob(i - 1))
            memo[i] = result
            return result

        return _rob(len(nums) - 1)