class NumArray {
    int[] sumArr;
    public NumArray(int[] nums) {
        sumArr = new int[nums.length+1];
        for(int i =0;i<nums.length;i++){
            sumArr[i+1] = sumArr[i] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        return sumArr[right + 1] - sumArr[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */