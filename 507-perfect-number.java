class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num<=1) return false;

        int upper_limit = (int)Math.pow(num,0.5);
        int ans = 1;
        for(int i=2;i<=upper_limit;i++){
            if(num%i==0){
                ans+=i;
                if(i != num/i) ans+= num/i;
            }
        }
        return num == ans;
    }
}