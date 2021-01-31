
def wiggleMaxLength(nums) -> int:
    if len(nums) < 2:
        return len(nums)
    l = []
    up = 1
    down = 1
    maxl = 2
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            up = down + 1
        if nums[i] > nums[i+1]:
            down = up + 1
    return max(up, down)


if __name__ == '__main__':
    print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))