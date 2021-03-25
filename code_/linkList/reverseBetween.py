"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        vhead = ListNode(val=None, next=head)
        # 左部分终点和右部分起点指针
        pre = suf = vhead

        for _ in range(1, left):
            pre = pre.next
        for _ in range(right):
            suf = suf.next
        # 工作指针
        leftp, rightp = pre.next, pre.next.next

        # 断开链表
        tail, suf.next, suf = leftp, None, suf.next

        # 逆置中间部分
        while rightp:
            rightp.next, leftp, rightp = leftp, rightp, rightp.next
            
        # 重新连接链表
        tail.next, pre.next = suf, leftp
        return vhead.next

if __name__ == '__main__':
    li = [3,5,1]
    left = 1
    right = 2
    head = ListNode(val=li[0])
    h = head
    for i in li[1:]:
        h.next = ListNode(val=i)
        h = h.next
    solution = Solution()
    head = solution.reverseBetween(head, left, right)
    # head = head.next
    while head:
        print(head.val)
        head = head.next