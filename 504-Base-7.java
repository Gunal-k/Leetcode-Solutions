class Solution {
    public String convertToBase7(int num) {
        if(num==0) return "0";

        String ans = "";
        int num_temp = num;
        num = Math.abs(num);
        while(num>0){
            ans = String.valueOf(num%7) + ans;
            num /= 7;
        }
        return num_temp<0 ? ("-"+ans) : ans;
    }
}