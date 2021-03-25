from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n <= 1:
            return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        d = [envelopes[0][1]]
        for i in range(1, n):
            if envelopes[i][1] > d[-1]:
                d.append(envelopes[i][1])
            else:
                if d[0] > envelopes[i][1]:
                    d[0] = envelopes[i][1]
                else:
                    high, low = len(d) - 1, 0
                    while high > low:
                        mid = (high + low) >> 1
                        if d[mid] < envelopes[i][1]:
                            low = mid + 1
                        else:
                            high = mid
                    d[low] = envelopes[i][1]
        return len(d)


if __name__ == '__main__':
    envelopes = [[15, 8], [2, 20], [2, 14], [4, 17], [8, 19], [8, 9], [5, 7], [11, 19], [8, 11], [13, 11], [2, 13],
                 [11, 19], [8, 11], [13, 11], [2, 13], [11, 19], [16, 1], [18, 13], [14, 17], [18, 19]]
    solution = Solution()
    print(solution.maxEnvelopes(envelopes))
