/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        int lh = left_height(root);
        int rh = right_height(root);

        if(lh==rh) return (1 << rh) -1;
        return this.countNodes(root.left) + this.countNodes(root.right) + 1;
    }

    private int left_height(TreeNode node){
        int h =0;
        while(node != null){
            h++;
            node = node.left;
        }
        return h;
    }

    private int right_height(TreeNode node){
        int h =0;
        while(node != null){
            h++;
            node = node.right;
        }
        return h;
    }
}