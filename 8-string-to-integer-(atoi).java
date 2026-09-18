class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty())
            return 0;

        int sign = 1, i = 0;

        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (s.charAt(i) == '+')
            i++;

        long ans = 0;

        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            long val = ans * 10 + (s.charAt(i) - '0');
            if (val > 2147483647) {
                return sign > 0 ? 2147483647 : -2147483648;
            }
            ans = val;
            i++;
        }
        return (int) (ans * sign);
    }
}
