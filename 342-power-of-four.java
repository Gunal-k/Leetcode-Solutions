class Solution {
    public boolean isPowerOfFour(int n) {
        // return n >0 && (Math.log(n) / Math.log(4)) % 1 == 0;

        if(n<=0) {
            return false;
        }
        while(n%4==0) {
            n = n/4;
        }
        return n == 1;
    }
}