class Solution {
    public String[] findWords(String[] words) {
        List<String> ans = new ArrayList<>();
        Map<Character, Integer> mp = new HashMap<>();
        mp.put('q', 1);
        mp.put('w', 1);
        mp.put('e', 1);
        mp.put('r', 1);
        mp.put('t', 1);
        mp.put('y', 1);
        mp.put('u', 1);
        mp.put('i', 1);
        mp.put('o', 1);
        mp.put('p', 1);
        mp.put('a', 2);
        mp.put('s', 2);
        mp.put('d', 2);
        mp.put('f', 2);
        mp.put('g', 2);
        mp.put('h', 2);
        mp.put('j', 2);
        mp.put('k', 2);
        mp.put('l', 2);
        mp.put('z', 3);
        mp.put('x', 3);
        mp.put('c', 3);
        mp.put('v', 3);
        mp.put('b', 3);
        mp.put('n', 3);
        mp.put('m', 3);

        for(String word: words){
            String s = word.toLowerCase();
            int target = mp.get(s.charAt(0));
            boolean valid = true;

            for (char ch : s.toCharArray()) {
                if (target != mp.get(ch)) {
                    valid = false;
                    break;
                }
            }

            if (valid)
                ans.add(word);
        }
        return ans.toArray(new String[0]);
    }
}