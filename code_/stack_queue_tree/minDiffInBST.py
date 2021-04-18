"""
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans, pre = [float('inf')], -1
        def dfs(root, pre, ans):
            if not root:
                return
            dfs(root.left, pre, ans)
            print(root.val)
            if pre != -1:
                ans[0] = min(root.val - pre, ans[0])
                # print(ans)
            pre = root.val
            dfs(root.right, pre, ans)
        dfs(root, pre, ans)
        return ans[0]


if __name__ == "__main__":
    root = [27, None, 34, None, 58, 50, None, 44, None]
    treeNodes = [TreeNode(val=i) if i != None else None for i in root]
    for i, v in enumerate(treeNodes[1:]):
        if treeNodes[i//2] is not None:
            if i % 2 == 0:
                treeNodes[i // 2].left = v
            else:
                treeNodes[i // 2].right = v
    solution = Solution()
    print(solution.minDiffInBST(treeNodes[0]))
