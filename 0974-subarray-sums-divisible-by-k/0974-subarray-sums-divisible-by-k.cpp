class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> freq(k, 0);
        freq[0] = 1;
        int sum = 0;
        int ans = 0;

        for(int i=0; i<nums.size(); i++) {
            sum = (sum + nums[i] % k + k) % k;
            ans += freq[sum];
            freq[sum]++;
        }

        return ans;   
    }
};