"""
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如"1,,3" 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
思路：递归验证左右子树是否合法，若左子树合法则将指针移动到右子树起始处
"""
from typing import List


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        if preorder[0] == '#':
            return True if len(preorder) == 1 else False

        left_start, right_start, end = 1, -1, 0

        right_start, validated = self.validate(preorder, left_start)
        if validated:
            end, validated = self.validate(preorder, right_start)

        return validated if end == len(preorder) else False
    
    def validate(self, preorder: List[str], start: int):
        if len(preorder[start:]):
            if preorder[start] == '#':
                return start + 1, True
            else:
                start, validated = self.validate(preorder, start + 1)
                if validated:
                    start, validated = self.validate(preorder, start)
                    return start, validated
        return -1, False


if __name__ == '__main__':
    # s = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    s = "#"
    solution = Solution()
    print(solution.isValidSerialization(s))
