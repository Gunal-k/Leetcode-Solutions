class Solution {
    Map<Integer,Integer> freq = new HashMap<>();
    public int[] findMode(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        dfs(root);
        int great = Collections.max(freq.values());
        for(int num : freq.keySet()){
            if(freq.get(num) == great) ans.add(num);
        }
        int[] res = new int[ans.size()];
        for(int i= 0 ;i<ans.size();i++){
            res[i] = ans.get(i);
        }
        return res;
    }
    public void dfs(TreeNode root){
        if(root == null) return;
        freq.put(root.val,freq.getOrDefault(root.val,0)+1);
        dfs(root.left);
        dfs(root.right);
    }
}