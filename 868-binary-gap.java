class Solution {
    public int binaryGap(int n) {
        String val = Integer.toBinaryString(n);
        int index = -1;
        int ans = 0;
        for(int i=0;i<val.length();i++){
            if(val.charAt(i) == '1'){
                if(index != -1){
                    int temp = i - index;
                    ans = temp > ans ? temp: ans;
                }
                index = i;
            }
        }
        return ans;
    }
}
