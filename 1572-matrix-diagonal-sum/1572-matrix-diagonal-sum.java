class Solution {
    public int diagonalSum(int[][] mat) {
        int r = mat.length;
        int c = mat[0].length;
        int sum = 0;
        
        for(int i = 0; i < r; i ++)
        {
                
            int primaryDiagonal = mat[i][i];
            int secondaryDiagonal = mat[i][c - i - 1];
            sum +=  primaryDiagonal;
            if(i != (c - i - 1) )
                sum += secondaryDiagonal;
            
        }
        
        return sum;
        
    }
}