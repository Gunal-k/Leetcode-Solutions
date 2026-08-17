class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> freq = new HashMap<>();

        String[] words = (s1 + " " + s2).split(" ");

        for (String word : words) {
            freq.put(word, freq.getOrDefault(word, 0) + 1);
        }

        List<String> ans = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            if (entry.getValue() == 1) {
                ans.add(entry.getKey());
            }
        }

        return ans.toArray(new String[0]);
        
    }
}
