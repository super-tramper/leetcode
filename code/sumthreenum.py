import sys

nums = []
for line in sys.stdin:
    if line.strip() != '':
        nums.append(int(line.strip()))
    else:
        break
nums.sort()
i = 0
j = 0
ret = []
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                if [nums[i], nums[j], nums[k]] not in ret:
                    ret.append([nums[i], nums[j], nums[k]])
                    print(nums[i], nums[j], nums[k])
