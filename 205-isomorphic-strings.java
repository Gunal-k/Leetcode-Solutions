class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character,Character> mapSt = new HashMap<>();
        Map<Character,Character> mapTs = new HashMap<>();

        for(int i =0 ; i<s.length();i++){
            char c1 = s.charAt(i), c2 = t.charAt(i);
            if(!mapSt.containsKey(c1)) mapSt.put(c1,c2);
            else if(mapSt.get(c1)!=c2) return false;
            if(!mapTs.containsKey(c2)) mapTs.put(c2,c1);
            else if(mapTs.get(c2)!=c1) return false;
        }
        return true;
    }
}