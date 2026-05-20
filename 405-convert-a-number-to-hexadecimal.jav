class Solution {
    public String toHex(int num) {
        if(num == 0) return "0";
        String map = "0123456789abcdef";
        String res = "";

        while(num!=0){
            res = map.charAt((num&15)) + res;
            num >>>= 4;
        }
        return res;
    }
}