from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # ans = [0]
        # for i in range(1, num + 1):
        #     # i & (i-1) 去掉了i最右边的1(若有)
        #     ans.append(ans[i & (i - 1)] + 1)
        # return ans
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans


if __name__ == '__main__':
    num = 5
    solution = Solution()
    print(solution.countBits(num))
