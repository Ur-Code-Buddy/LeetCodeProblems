class Solution {
    public int maximumWealth(int[][] accounts) {
        int maximum_wealth = 0;

        for(int[] account : accounts)
        {
            int sum = 0;
            for (int wealth : account)
                sum += wealth; 
            maximum_wealth = Math.max(sum, maximum_wealth);
        }
        return maximum_wealth;
        
    }
}