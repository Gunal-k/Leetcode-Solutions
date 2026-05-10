class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> result = new HashSet<>();
        Set<Integer> visited = new HashSet<>();
        for(int num: nums1){
            visited.add(num);
        }

        for(int num: nums2){
            if(visited.contains(num)){
                result.add(num);
            }
        }
        int[] ans = new int[result.size()];
        int i = 0;

        for (int num : result) {
            ans[i++] = num;
        }

        return ans;
    }
}