def maxArea(height):
    i = 0
    j = len(height) - 1
    maxarea = 0
    while i < j:
        area = (j - i) * min(height[i], height[j])
        maxarea = area if area > maxarea else maxarea
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxarea


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
