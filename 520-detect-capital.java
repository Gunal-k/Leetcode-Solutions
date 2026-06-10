class Solution {
    public boolean detectCapitalUse(String word) {
        int first_upper = 0, count = 0;
        int n = word.length();

        for(int i=0;i<n;i++){
            if(Character.isUpperCase(word.charAt(i))){
                count++;
                if(i==0) first_upper = 1;
                else first_upper = 2;
            }
        }
        
        if(count == 0) return true;
        else if(count == n) return true;
        else if(first_upper == 1) return true;
        else return false;
    }
}