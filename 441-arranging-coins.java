class Solution {
    public int arrangeCoins(int n) {
        int l = 1, r = n, ans = 0;
        while(l<=r){
            int mid = l+ (r-l)/2;
            long coins = (long) (mid*(mid+1) / 2);
            if(coins <= n){
                ans = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        return ans;
    }
}