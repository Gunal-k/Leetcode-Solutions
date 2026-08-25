class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int n = nums.length;
        int odd = 1;
        for (int i = 0; i < n; i += 2) {
            if (nums[i] % 2 == 1) {
                while (nums[odd] % 2 == 1) {
                    odd += 2;
                }
                int temp = nums[i];
                nums[i] = nums[odd];
                nums[odd] = temp;
            }
        }
        return nums;
    }
}
