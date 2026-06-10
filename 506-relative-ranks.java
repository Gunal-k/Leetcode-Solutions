class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        int[][] arr = new int[n][2];
        for(int i=0;i<n;i++){
            arr[i][0] = score[i];
            arr[i][1] = i;
        }
        Arrays.sort(arr, (a, b) -> b[0] - a[0]);
        String[] ans = new String[n];
        for(int i=0;i<n;i++){
            int temp = arr[i][1];
            if(i == 0) ans[temp] = "Gold Medal";
            else if(i == 1) ans[temp] = "Silver Medal";
            else if(i == 2) ans[temp] = "Bronze Medal";
            else ans[temp] = String.valueOf(i + 1);
        }
        return ans;
    }
}