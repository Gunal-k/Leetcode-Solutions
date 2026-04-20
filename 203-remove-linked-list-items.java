class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0,head);
        ListNode prev = dummy;
        ListNode cur = head;

        while(cur != null){
            ListNode nxt = cur.next;

            if(cur.val == val) prev.next = nxt;
            else prev = cur;
            cur = nxt;
        }
        return dummy.next;
    }
}