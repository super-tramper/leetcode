class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        if len(set(arr)) < 2:
            return 1
        maxl, length = 2, 2
        for i in range(1, len(arr) - 1):
            if arr[i - 1] == arr[i] or arr[i] == arr[i+1]:
                length = 2
                continue
            if int(arr[i] < arr[i - 1]) ^ int(arr[i] > arr[i + 1]):
                length += 1
                maxl = max(maxl, length)
            else:
                length = 2
        return maxl


if __name__ == '__main__':
    ar = [8, 8, 9, 10, 6, 8, 2, 4, 2, 2, 10, ]
    solution = Solution()
    print(solution.maxTurbulenceSize(ar))
