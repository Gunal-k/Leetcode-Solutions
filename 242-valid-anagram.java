class Solution {
    public boolean isAnagram(String s, String t) {
        // if(s.length() == t.length()){
        //     char[] a =s.toCharArray();
        //     char[] b = t.toCharArray();
        //     Arrays.sort(a);
        //     Arrays.sort(b);
        //     return Arrays.equals(a,b);
        // }
        // return false;

        // if (s.length() != t.length()) return false;

        // Map<Character, Integer> counts = new HashMap<>();
        // int n = s.length();

        // for (int i = 0; i < n; i++) {
        //     counts.put(s.charAt(i), counts.getOrDefault(s.charAt(i), 0) + 1);
        //     counts.put(t.charAt(i), counts.getOrDefault(t.charAt(i), 0) - 1);
        // }

        // for (int count : counts.values()) {
        //     if (count != 0) return false;
        // }

        // return true;

        if (s.length() != t.length()) return false;

        int[] a = new int[26];
        for (int i = 0; i < s.length(); i++) {
            a[s.charAt(i)-'a']++;
            a[t.charAt(i)-'a']--;
        }

        for (int count : a) {
            if (count != 0) return false;
        }

        return true;
    }
}