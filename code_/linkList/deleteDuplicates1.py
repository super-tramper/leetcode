"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        headNode = ListNode(val=None, next=head)
        work = headNode
        while work:
            if work.next and work.next.val == work.val:
                work.next = work.next.next
            else:
                work = work.next
        return headNode.next


if __name__ == '__main__':
    li = [1,2,3,3,4,4,5]
    head = ListNode(val=li[0])
    h = head
    for i in li[1:]:
        h.next = ListNode(val=i)
        h = h.next
    solution = Solution()
    head = solution.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next