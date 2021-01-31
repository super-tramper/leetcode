def findMedianSortedArrays(nums1, nums2):
    l = (len(nums1) + len(nums2) + 1) // 2
    r = (len(nums1) + len(nums2) + 2) // 2
    return (findKth(nums1, nums2, l) + findKth(nums1, nums2, r)) / 2


def findKth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        return findKth(nums2, nums1, k)
    if len(nums1) == 0:
        return nums2[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])
    i, j = min(len(nums1) - 1, k // 2 - 1), min(len(nums2) - 1, k // 2 - 1)
    if nums1[i] > nums2[j]:
        return findKth(nums1, nums2[j + 1:], k - j - 1)
    else:
        return findKth(nums1[i + 1:], nums2, k - i - 1)


if __name__ == '__main__':
    print(findMedianSortedArrays([2], []))
