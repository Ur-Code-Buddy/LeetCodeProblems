class Solution {
    Map<Integer, Integer> cache = new HashMap<>();
    public int climbStairs(int n) {
        
        if ( n==0 || n ==1 )return 1;
        if(cache.get(n) != null) return cache.get(n);
        
        
        int climb_one_steps = climbStairs(n-1);
        int climb_two_steps = climbStairs(n-2);
        int totalWays = climb_one_steps + climb_two_steps;
        cache.put(n, totalWays);
        return climb_one_steps + climb_two_steps;
    }
}