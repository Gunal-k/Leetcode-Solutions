class Solution {
    public int surfaceArea(int[][] grid) {
        int area = 0;
        int n = grid.length;

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] >0){
                    area += grid[i][j]*4+2;
                    if(j>0) area -= Math.min(grid[i][j-1],grid[i][j])*2;
                    if(i>0) area -= Math.min(grid[i-1][j],grid[i][j])*2;
                }
            }
        }
        return area;
    }
}
