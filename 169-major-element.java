class Solution {
        public int majorityElement(int[] nums) {
                int n = nums.length / 2;
                int ans = 0, mx = 0;
                Map<Integer, Integer> freq = new HashMap<>();
                for (int num : nums) {
                        if (freq.containsKey(num)) freq.put(num, freq.get(num) + 1);
                        else freq.put(num, 1);
                        if (freq.get(num) > n) mx = num;
                }
                return mx;
        }
}