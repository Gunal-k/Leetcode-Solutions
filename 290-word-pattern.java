class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length)
            return false;

        Map<Character, String> c_to_w = new HashMap<>();
        Map<String, Character> w_to_c = new HashMap<>();

        for (int i = 0; i < words.length; i++) {
            char c = pattern.charAt(i);
            String w = words[i];

            if (c_to_w.containsKey(c) && 
                !c_to_w.get(c).equals(w)) {
                return false;
            }

            if (w_to_c.containsKey(w) && 
                w_to_c.get(w) != c) {
                return false;
            }

            c_to_w.put(c, w);
            w_to_c.put(w, c);
        }
        return true;
    }
}