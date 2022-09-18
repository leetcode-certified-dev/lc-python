class Node:
    def __init__(self, key: int = 0, val: int = 0, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        front = Node()
        end = Node()
        front.next = end
        end.prev = front
        self.front = front
        self.end = end
        self.cap = capacity
        self.map = {}  # type map: Dict[int, Node]

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        if len(self.map) == self.cap:
            to_remove = self.end.prev
            del self.map[to_remove.key]
            self.remove(self.end.prev)

        new_node = Node()
        new_node.key = key
        new_node.val = value
        self.insert(new_node)
        self.map[key] = new_node

    def remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node):
        old_front = self.front.next
        self.front.next = node
        node.next = old_front
        old_front.prev = node
        node.prev = self.front

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
