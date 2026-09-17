class Solution {
    public int reverse(int x) {
        int s = x > 0 ? 1 : -1;
        int ans = 0;
        x *= s;
        while (x > 0) {
            int a = x % 10;
            long b = (long) ans * 10 + a;
            if (b <= 2147483647)
                ans = (int) b;
            else
                return 0;
            x /= 10;
        }
        return ans * s;
    }
}
