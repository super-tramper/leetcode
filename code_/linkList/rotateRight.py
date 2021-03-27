"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n, work = 0, head
        # 统计长度
        while work:
            work = work.next
            n += 1
        if n <= 1 or k % n == 0:
            return head
        # 逆转整个链表
        reversedList = self.reverseList(head)
        # 移动工作指针到第k个节点
        work = reversedList
        for _ in range(k%n-1):
            work = work.next
        # 断开链表
        l2_head = work.next
        work.next = None
        self.reverseList(reversedList)
        r2_head = self.reverseList(l2_head)
        reversedList.next = r2_head
        return work

    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    li = [1,2,3,4,5]
    k = 2
    head = ListNode(val=li[0])
    h = head
    for i in li[1:]:
        h.next = ListNode(val=i)
        h = h.next
    solution = Solution()
    head = solution.rotateRight(head, k)
    while head:
        print(head.val)
        head = head.next