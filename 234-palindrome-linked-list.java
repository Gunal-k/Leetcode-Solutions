/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // List<Integer> nums = new ArrayList<>();

        // while(head != null){
        //     nums.add(head.val);
        //     head = head.next;
        // }
        // int l = 0, r = nums.size() - 1;
        // System.out.println(nums);
        // while(l<=r){
        //     if(nums.get(l) != nums.get(r)){
        //         return false;
        //     }
        //     l++;
        //     r--;
        // }
        // return true;

        ListNode fast = head, slow = head;
        while(fast != null && fast.next != null){
            fast = fast.next;
            fast = fast.next;
            slow = slow.next;
        }

        ListNode prev = null;
        while(slow != null){
            ListNode tmp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = tmp;
        }

        ListNode left = head, right = prev;
        while(right != null){
            if(left.val != right.val){
                return false;
            }
            right = right.next;
            left = left.next;
        }
        return true;
    }
}