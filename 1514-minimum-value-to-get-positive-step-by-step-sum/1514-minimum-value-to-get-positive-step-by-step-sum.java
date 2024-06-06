class Solution {
    public int minStartValue(int[] nums) {
        int minSum = 0;
        int totalSum = 0;
        for (int i = 0; i < nums.length; i ++){
            totalSum = totalSum + nums[i];
            minSum = minSum < totalSum ? minSum : totalSum;
        }
        return -minSum + 1;
        
    }
}