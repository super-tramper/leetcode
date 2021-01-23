# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode):
    remain = 0
    ptr = None
    ptr1 = l1
    ptr2 = l2
    s = ''
    if l1 and l2:
        remain = (ptr1.val + ptr2.val) // 10
        head = ListNode(val=(l1.val + l2.val) % 10)
        ptr = head
        s += str(ptr.val)
    ptr1, ptr2 = ptr1.next, ptr2.next
    while ptr1 and ptr2:
        ptr.next = ListNode(val=((ptr1.val + ptr2.val + remain) % 10))
        remain = (ptr1.val + ptr2.val + remain) // 10
        s += str(ptr.next.val)
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        ptr = ptr.next
    while ptr1:
        ptr.next = ListNode(val=(ptr1.val + remain) % 10)
        remain = (ptr1.val + remain) // 10
        s += str(ptr.next.val)
        ptr, ptr1 = ptr.next, ptr1.next
    while ptr2:
        ptr.next = ListNode(val=(ptr2.val + remain) % 10)
        remain = (ptr2.val + remain) // 10
        s += str(ptr.next.val)
        ptr, ptr2 = ptr.next, ptr2.next
    if remain:
        ptr.next = ListNode(val=remain)
    return head


if __name__ == '__main__':
    head1 = ListNode(val=2, next=ListNode(val=4))
    head2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    print(addTwoNumbers(head1, head2))
