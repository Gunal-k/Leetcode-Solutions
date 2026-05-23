class Solution {
    public List<String> commonChars(String[] words) {
        Map<Character,Integer> freq1 = new HashMap<>();
        for(Character ch:words[0].toCharArray()){
            freq1.put(ch,freq1.getOrDefault(ch,0)+1);
        }
        
        for(String word : words){
            Map<Character,Integer> freq2 = new HashMap<>();
            for(Character ch:word.toCharArray()){
                freq2.put(ch,freq2.getOrDefault(ch,0)+1);
            }
            for(Character ch:freq1.keySet()){
                if(freq2.containsKey(ch)){
                    freq1.put(ch,Math.min(freq1.get(ch),freq2.get(ch)));
                }
                else freq1.put(ch,0);
            }
        }

        List<String> ans = new ArrayList<>();
        for(Character ch:freq1.keySet()){
            for(int i=0;i<freq1.get(ch);i++){
                ans.add(String.valueOf(ch));
            }
        }
        return ans;
    }
}