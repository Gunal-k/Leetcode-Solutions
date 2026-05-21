class Solution {
    public int longestPalindrome(String s) {
        Map<Character,Integer> freq = new HashMap<>();
        for(char ch : s.toCharArray()){
            freq.put(ch,freq.getOrDefault(ch,0)+1);
        }
        int ans = 0;
        boolean odd = false;

        for(int num : freq.values()){
            if(num % 2 == 1) odd = true;
            ans += num - (num % 2);
        }
        return odd?ans+1:ans;
    }
}