"""
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashmap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 769
        self.map = [[] for _ in range(self.length)]

    def put(self, key: int, value: int) -> None:
        ord_key = sum([ord(i) for i in str(key)])%self.length
        flag = True
        for index, kv in enumerate(self.map[ord_key]):
            if kv[0] == key:
                flag = False
                self.map[ord_key][index] = [key, value]
        if flag:
            self.map[ord_key].append([key, value])

    def remove(self, key: int) -> None:
        ord_key = sum([ord(i) for i in str(key)])%self.length
        for index, kv in enumerate(self.map[ord_key]):
            if kv[0] == key:
                self.map[ord_key].pop(index)
            
    def get(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        ord_key = sum([ord(i) for i in str(key)])%self.length
        for index, kv in enumerate(self.map[ord_key]):
            if kv[0] == key:
                return self.map[ord_key][index][1]
        return -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    print(obj.get(3))
    obj.put(2, 1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))