from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


if __name__ == "__main__":
    root = [7, 3, 15, None, None, 9, 20]
    treeNodes = [TreeNode(val=i) if i != None else None for i in root]
    for i, v in enumerate(treeNodes[1:]):
        if i % 2 == 0:
            treeNodes[i//2].left = v
        else:
            treeNodes[i//2].right = v
    solution = Solution()
    print(solution.inorderTraversal(treeNodes[0]))
