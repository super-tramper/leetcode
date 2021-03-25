"""
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashset
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 769
        self.map = [[] for _ in range(self.length)]

    def add(self, key: int) -> None:
        ord_key = sum([ord(i) for i in str(key)])%self.length
        if key not in self.map[ord_key]:
            self.map[ord_key].append(key)

    def remove(self, key: int) -> None:
        ord_key = sum([ord(i) for i in str(key)])%self.length
        if key in self.map[ord_key]:
            self.map[ord_key].remove(key)
            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        ord_key = sum([ord(i) for i in str(key)])%self.length
        if key in self.map[ord_key]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.add(2)
    obj.remove(1)
    param_2 = obj.contains(1) 
    param_3 = obj.contains(2) 
    print(param_2, param_3)