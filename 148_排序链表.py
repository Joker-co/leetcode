# 148. 排序链表
# 时间复杂度要求O(nlogn)
# 使用归并排序
# 难点在于链表为单向链表，索引节点时间复杂度为O(n)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 为链表添加头结点，记录头节点
        res = ListNode(0)
        res.next = head
        # 统计链表长度
        length = 0
        while head: head, length = head.next, length+1

        # 初始化待排序子链表长度
        path = 1
        while path<length:
            # h为开始比对的两个子链表的首部
            pre, h = res, res.next
            # 直到没有接下来可排序的两个子链表
            while h:
                h1, i = h, path
                while h and i: h, i = h.next, i-1
                if i: break
                h2, i = h, path
                while h and i: h, i = h.next, i-1
                p1, p2 = path, path-i
                while p1 and p2:
                    if h1.val<h2.val: pre.next, h1, p1 = h1, h1.next, p1-1
                    else: pre.next, h2, p2 = h2, h2.next, p2-1 
                    pre = pre.next
                pre.next = h1 if p1 else h2
                while p1>0 or p2>0: pre, p1, p2 = pre.next, p1-1, p2-1
                pre.next = h
            path *= 2
        return res.next
