class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        char[] arr = s.toCharArray();
        for (char ch : arr) {
            count[ch - 'a']++;
        }
        for (int i=0;i<s.length();i++) {
            if (count[arr[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}