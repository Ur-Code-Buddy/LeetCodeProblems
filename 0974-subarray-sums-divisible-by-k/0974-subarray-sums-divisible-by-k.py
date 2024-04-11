class Solution(object):
    def subarraysDivByK(self, nums, k):
        freq = [0] * k
        freq[0] = 1
        sum = 0
        ans = 0

        for num in nums:
            sum = (sum + num % k + k) % k
            ans += freq[sum]
            freq[sum] += 1

        return ans
