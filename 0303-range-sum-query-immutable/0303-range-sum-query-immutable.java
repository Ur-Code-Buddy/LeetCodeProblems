class NumArray {
    private ArrayList<Integer> prefix_sum;

    public NumArray(int[] nums) {
        
        prefix_sum = new ArrayList<>();
        prefix_sum.add(0);
        int length = nums.length;

        int temp_sum = 0;
        for (int i = 0; i < length; i++){
            temp_sum = nums[i] + temp_sum;
            prefix_sum.add(temp_sum);
        }
        
    }
    
    public int sumRange(int left, int right) {

        return prefix_sum.get(right + 1) - prefix_sum.get(left);
        
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */