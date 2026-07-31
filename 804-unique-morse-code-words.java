class Solution {
    String[] arr = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    public int uniqueMorseRepresentations(String[] words) {
        Set<String> Transf = new HashSet<>();
        for(String word : words){
            String form = "";
            for(Character ch : word.toCharArray()){
                form += arr[(int)ch-(int)'a'];
            }
            Transf.add(form);
        }
        return Transf.size();
    }
}
