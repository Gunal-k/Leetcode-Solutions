class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer,Integer> freq = new HashMap<>();
        List<Integer> ans =  new ArrayList<>();

        for(int num : nums1){
            freq.put(num,freq.getOrDefault(num,0)+1);
        }

        for(int num : nums2){
            if(freq.containsKey(num) && freq.getOrDefault(num,0)>0){
                freq.put(num,freq.get(num)-1);
                ans.add(num);
            }
        }
        int[] res = new int[ans.size()];
        int i = 0;

        for (int num : ans) {
            res[i++] = num;
        }

        return res;
    }
}