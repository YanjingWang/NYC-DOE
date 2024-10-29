class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        # Using two dummy nodes head and tail to make insertion and deletion easier.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            # Remove the node and move it to the front.
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self._remove(self.hash_map[key])
        node = Node(key, value)
        self._add(node)
        self.hash_map[key] = node
        # If the cache has exceeded its capacity, remove the least recently used item.
        if len(self.hash_map) > self.capacity:
            node_to_remove = self.head.next
            self._remove(node_to_remove)
            del self.hash_map[node_to_remove.key]

    def _add(self, node: Node) -> None:
        """Helper function to add a node right before the tail node."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node: Node) -> None:
        """Helper function to remove a node from the list."""
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    test = LRUCache(2)
    test.put(1, 1)
    test.put(2, 2)
    print(test.get(1))
    test.put(3, 3)
    print(test.get(2))
    test.put(4, 4)
    print(test.get(1))
    print(test.get(3))
    print(test.get(4))
    print(test.get(2))
    print(test.get(1))
    print(test.get(3))
    print(test.get(4))
    print(test.get(2))
    print(test.get(1))
    print(test.get(3))
    print(test.get(4))
    print(test.get(2))
    print(test.get(1))
    print(test.get(3))
    print(test.get(4))
    print(test.get(2))
