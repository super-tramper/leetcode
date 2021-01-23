class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x) -> ListNode:
    head_small = ListNode(None)
    head_big = ListNode(None)
    hs = head_small
    hb = head_big
    while head:
        if head.val < x:
            head_small.next = head
            head_small = head_small.next
        else:
            head_big.next = head
            head_big = head_big.next
        head = head.next
    head_small.next = hb.next
    head_big.next = None
    return hs.next


if __name__ == '__main__':
    head1 = ListNode(1)
    head2 = ListNode(4)
    head3 = ListNode(3)
    head4 = ListNode(2)
    head5 = ListNode(5)
    head6 = ListNode(2)
    head = head1
    head1.next = head2
    head2.next = head3
    head3.next = head4
    head4.next = head5
    head5.next = head6
    ret = partition(head, 3)
    while ret.next != None:
        print(ret.val)
        ret = ret.next
    print(ret.val)
