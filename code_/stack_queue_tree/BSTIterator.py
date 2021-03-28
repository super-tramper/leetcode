"""
实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
int next()将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        treeNodes = [TreeNode(val=i) if i != None else None for i in root]
        self.root = treeNodes[0]
        for i, v in enumerate(treeNodes[1:]):
            if i % 2 == 0:
                treeNodes[i//2].left = v
            else:
                treeNodes[i//2].right = v
        self.sortedList = []
        self.inorder(treeNodes[0])
        print(self.sortedList)
        
    def next(self) -> int:
        return self.sortedList.pop(0)

    def hasNext(self) -> bool:
        return len(self.sortedList) > 0
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.sortedList.append(node.val)
        self.inorder(node.right)


# Your BSTIterator object will be instantiated and called as such:
if __name__ == "__main__":
    root = [7, 3, 15, None, None, 9, 20]
    obj = BSTIterator(root)
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())