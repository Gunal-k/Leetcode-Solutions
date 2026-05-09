class Solution {
    public String reverseVowels(String s) {
        int l =0, r = s.length() -1;
        char[] alpha = s.toCharArray();

        while(l<r){
            if(isVowel(alpha[l])){
                if(isVowel(alpha[r])){
                    char temp = alpha[l];
                    alpha[l] = alpha[r];
                    alpha[r] = temp;
                    l++;
                    r--;
                }
                else{
                    r--;
                }
            }
            else{
                l++;
            }
        }
        return String.valueOf(alpha);
    }

    public boolean isVowel(char ch){
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U'){
            return true;
        }
        return false;
    }

}