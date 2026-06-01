class Solution {
    public int[] constructRectangle(int area) {
        int w = (int)Math.sqrt(area);
        while(area%w!=0){
            w--;
        }
        int val = area/w;
        return new int[] {val,w};
    }
}