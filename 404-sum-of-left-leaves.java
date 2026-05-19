class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root,false);
    }
    private int dfs(TreeNode node, boolean flag){
        int ans = 0;
        if(node == null) return 0;
        if(node.left == null && node.right == null) return flag?node.val:0;
        ans += dfs(node.left,true);
        ans += dfs(node.right,false);
        return ans;
    }
}