class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer,Integer> idx = new HashMap<>();
        for(int i=0;i<nums1.length;i++){
            idx.put(nums1[i],i);
        }

        int[] ans = new int[nums1.length];
        Arrays.fill(ans,-1);
        
        Stack<Integer> res = new Stack<>();

        for(int i =0;i<nums2.length;i++){
            int curr = nums2[i];
            while(!res.isEmpty() && curr > res.peek()){
                int val = res.pop();
                int index = idx.get(val);
                ans[index] = curr;
            }
            if(idx.containsKey(curr)){
                res.push(curr);
            }
        }
        return ans;
    }
}