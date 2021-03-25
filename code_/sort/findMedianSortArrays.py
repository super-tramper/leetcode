# 给定两个大小为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的中位数。
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
# 时间复杂度O(n)
def findMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    ret_list = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ret_list.append(nums1[i])
            i += 1
        else:
            ret_list.append(nums2[j])
            j += 1
    if i < len(nums1):
        ret_list.extend(nums1[i:])
    if j < len(nums2):
        ret_list.extend(nums2[j:])
    return (ret_list[(len(ret_list) + 1) // 2 - 1] + ret_list[(len(ret_list) + 2) // 2 - 1]) / 2
    # return ret_list[len(ret_list) // 2] if len(ret_list) % 2 else (ret_list[len(ret_list) // 2 - 1] + ret_list[
    #     len(ret_list) // 2]) / 2


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 3], [2]))

# 0 - 5 2 3  6
# 0 - 6 3  7
