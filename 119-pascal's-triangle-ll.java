class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> triangle = new ArrayList<>();
        triangle.add(1);

        for(int i=0;i<rowIndex;i++){
            List<Integer> prev =new ArrayList<>();
            for(int j=0;j<triangle.size()-1;j++){
                prev.add(triangle.get(j) + triangle.get(j+1));
            }
            triangle.clear();
            triangle.addAll(prev);
            triangle.add(0,1);
            triangle.add(1);
        }
        return triangle;
    }
}