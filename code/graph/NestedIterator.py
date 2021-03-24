# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.ret = []
        self.dfs(nestedList)

    def next(self) -> int:
        return self.ret.pop(0)

    def hasNext(self) -> bool:
        return bool(len(self.ret))

    def dfs(self, nestedList):
        for i in nestedList:
            if isinstance(i, int):
                self.ret.append(i)
            else:
                self.dfs(i)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    i, v = NestedIterator([[1, 1], 2, [1, 1]]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
