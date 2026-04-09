class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        for(int i=0;i<numRows;i++){
            List<Integer> prev =new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0 || j == i){
                    prev.add(1);
                }
                else{
                    int val = triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j);
                    prev.add(val);
                }
            }
            triangle.add(prev);
        }
        return triangle;
    }
}