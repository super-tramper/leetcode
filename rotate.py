def rotate(nums, k) -> None:
    k = k % len(nums)
    return nums[::-1][0:k][::-1] + nums[::-1][k:][::-1]


# def invrese(nums, start, end):
#     while start < end:
#         nums[start], nums[end] = nums[end], nums[start]
#         start, end = start + 1, end - 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
