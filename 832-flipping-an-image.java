class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        int m = image[0].length;
        int[][] ans = new int[n][m];
        for(int i = 0;i < n;i++){
            for(int j = m-1;j >= 0;j--){
                ans[i][m-j-1] = 1- image[i][j];
            }
        }
        return ans;
    }
}
