class Solution {
    TreeNode ans;
    public TreeNode increasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode();
        ans = dummy;
        dfs(root);
        return dummy.right;
    }
    private void dfs(TreeNode node){
        if(node == null) return;
        dfs(node.left);
        ans.right = new TreeNode(node.val);
        ans = ans.right;
        dfs(node.right);
    }
}
