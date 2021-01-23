def checkStraightLine(coordinates):
    n = len(coordinates)
    x1 = coordinates[0][0] - coordinates[1][0]
    y1 = coordinates[0][1] - coordinates[1][1]
    for i in range(2, n - 1):
        xx = coordinates[i][0] - coordinates[0][0]
        yy = coordinates[i][1] - coordinates[0][1]
        if x1 * yy != xx * y1:
            return False
    return True


if __name__ == '__main__':
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(checkStraightLine(coordinates))
