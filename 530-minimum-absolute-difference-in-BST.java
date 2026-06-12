class Solution {
    int ans = Integer.MAX_VALUE;
    Integer prev = null;
    public int getMinimumDifference(TreeNode root) {
        dfs(root);
        return ans;
    }
    public void dfs(TreeNode node){
        if(node == null){
            return;
        }
        dfs(node.left);
        if(prev != null){
            ans = Math.min(ans,node.val - prev);
        }
        prev = node.val;
        dfs(node.right);
    }
}