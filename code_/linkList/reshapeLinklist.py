class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reshapeLinklist(pointer):
    p1, p2 = pointer, pointer
    # 用两个指针遍历链表，p1最终指向链表的中间位置
    while p2.next:
        p2 = p2.next
        if p2.next: p2 = p2.next
        else: break
        p1 = p1.next
    # p3指向整个链表的起点， p4指向后半段链表的起点
    p3, p4 = pointer, p1.next
    # 从中间断开链表并将后半段逆置，p4指向逆置后的链表起点
    p1.next, p4 = None, reverse(p4)
    # 将后半段链表中的节点依次插入前半段的相应位置
    while p3 and p4:
        temp, p4 = p4, p4.next
        temp.next = p3.next
        p3.next, p3 = temp, temp.next
    return pointer


def reverse(pointer):
    p1, p2 = pointer, pointer.next
    p1.next = None
    while p2:
        temp = p1
        p1, p2 = p2, p2.next
        p1.next = temp
    return p1


if __name__ == '__main__':
    n5 = LinkNode(5)
    n4 = LinkNode(4, n5)
    n3 = LinkNode(3, n4)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(1, n2)
    pointer = LinkNode(0, n1)
    ret = reshapeLinklist(pointer)
    while ret:
        print(ret.data)
        ret = ret.next
