class Solution {
    public String reverseVowels(String s) {
        int l =0, r = s.length() -1;
        char[] alpha = s.toCharArray();

        while(l<r){
            while(l<r && ! isVowel(alpha[l])){
                l++;
            }
            while(l<r && ! isVowel(alpha[r])){
                r--;
            }
            char temp = alpha[l];
            alpha[l] = alpha[r];
            alpha[r] = temp;
            l++;
            r--;
        }
        return String.valueOf(alpha);
    }

    public boolean isVowel(char ch){
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }

}