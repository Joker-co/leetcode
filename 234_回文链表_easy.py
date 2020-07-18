class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        pre, cur = None, None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next

            cur.next = pre
            pre = cur
        
        if fast:
            slow = slow.next
        while(cur):
            if cur.val!=slow.val:
                return False
            cur = cur.next
            slow = slow.next
        return True
