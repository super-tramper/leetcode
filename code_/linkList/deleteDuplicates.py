"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        headNode = ListNode(val=None, next=head)
        pre, work = headNode, head
        while work:
            flag = True
            temp = work
            while work.next and work.val == work.next.val:
                flag = False
                work = work.next
            work = work.next
            if flag:
                pre = temp
            else:
                pre.next = work
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
