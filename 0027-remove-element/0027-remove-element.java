class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            // Skip elements from the right that are equal to val
            while (right >= 0 && nums[right] == val) {
                right--;
            }
            
            // If the current left element is equal to val, replace it with the element from the right
            if (left <= right && nums[left] == val) {
                nums[left] = nums[right];
                right--;  // Decrement right as we have moved an element from the right to left
            }
            left++;  // Move to the next element from the left
        }

        return right + 1;  // The new length of the array without val elements
    }
}
