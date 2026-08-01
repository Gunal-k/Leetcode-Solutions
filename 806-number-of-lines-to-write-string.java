class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int lines = 1, width = 0;
        for(char ch : s.toCharArray()){
            int pixels = widths[ch - 'a'];
            if((width+ pixels)>100){
                lines++;
                width = 0;
            }
            width += pixels;
        }
        return new int[]{lines,width};
    }
}
