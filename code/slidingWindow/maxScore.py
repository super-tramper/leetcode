# 求出滑动窗口内（长度为n-k）元素和的最小值，剩余元素的最小值
class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        # 计算出数组前k项的和
        minScore = sum(cardPoints[:n - k])
        sumn = sumWindow = minScore
        # 向后移动窗口，不断更新窗口内元素的和，更新窗口和的最小值
        for i in range(n - k, n):
            sumWindow = sumWindow + cardPoints[i] - cardPoints[i + k - n]
            minScore = min(minScore, sumWindow)
            sumn += cardPoints[i]
        return sumn - minScore


if __name__ == '__main__':
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    solution = Solution()
    print(solution.maxScore(cardPoints, k))
