class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] delta = new int[n+1];

        for(int[] pair:trust){
            int src = pair[0];
            int dst = pair[1];
            delta[src]--;
            delta[dst]++;
        }
        for(int i=1;i<n+1;i++){
            if(delta[i]==n-1) return i;
        }
        return -1;
    }
}
