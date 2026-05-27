class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String double_s = (s + s).substring(1,(s.length()*2)-1);
        return double_s.contains(s);
    }
}