def canPlaceFlowers(flowerbed, n) -> bool:
    prev = -1
    count = 0
    m = len(flowerbed)
    for index, i in enumerate(flowerbed):
        if i:
            if prev == -1:
                if index >= 2:
                    count += index >> 1
            else:
                count += (index - prev - 2) >> 1
            prev = index
        if count >= n:
            return True
    if m - prev >= 2:
        count += (m - prev - 1) >> 1
    if prev == -1:
        count = (m + 1) >> 1
    return count >= n


if __name__ == '__main__':
    flowers = [0, 0, 0, 0, 0]
    print(canPlaceFlowers(flowers, 1))
