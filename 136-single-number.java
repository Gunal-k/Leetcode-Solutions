class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for(Integer num : nums){
            ans ^= num;
        }
        return ans;
    }
}