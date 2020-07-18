# 迭代法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        
        pre = None
        cur = head
        post = head.next
        while post:
            cur.next = pre
            pre = cur
            cur = post
            post = post.next
        cur.next = pre
        return cur

# 递归法
def moni(pre, cur):
    if not cur:
        return pre
    post = cur.next
    cur.next = pre
    return moni(cur, post)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        new_head = moni(None, head)
        return new_head
