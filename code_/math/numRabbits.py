"""
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。

返回森林中兔子的最少数量。
answers 的长度最大为1000。
answers[i] 是在 [0, 999] 范围内的整数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rabbits-in-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
相同答案n的兔子可以归到同一组，该组内最多有n+1只兔子，若兔子数量超过n+1，则分裂出新组，可用字典和数组完成计算
"""
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums = [0]*1000
        result = 0
        for i in answers:
            if nums[i] == 0:
                nums[i] = i + 1
                result += i + 1
            nums[i] -= 1
        return result


if __name__ == '__main__':
    answers = [10, 10, 10]
    solution = Solution()
    print(solution.numRabbits(answers))
