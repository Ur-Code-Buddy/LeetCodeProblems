class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int leftPtr = 0;
        int rightPtr = numbers.length - 1;

        while (leftPtr < rightPtr){

            if (numbers[leftPtr] + numbers[rightPtr] == target){
                return new int[]{leftPtr + 1,rightPtr + 1};
            }

            if (numbers[leftPtr] + numbers[rightPtr] > target)
            {
                rightPtr --;
            }
            else {
                leftPtr ++;
            }
        }
        return new int[]{}; 
    } 
}