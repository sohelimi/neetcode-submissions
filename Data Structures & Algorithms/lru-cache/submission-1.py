
class Node:
    """Doubly linked list node to store key-value pairs."""
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key -> node for O(1) access

        # Dummy head and tail to simplify edge cases in the doubly linked list
        self.head = Node(0, 0)  # Most recently used will be right after head
        self.tail = Node(0, 0)  # Least recently used will be right before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Unlink 'node' from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert_at_front(self, node: Node):
        """Insert 'node' right after head (mark as most recently used)."""
        # head -> node -> first_real
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def get(self, key: int) -> int:
        """
        Return value if key exists; otherwise -1.
        Move the accessed node to the front (mark as most recently used).
        """
        if key in self.cache:
            node = self.cache[key]
            # Move to MRU: remove from current position and re-insert at front
            self._remove(node)
            self._insert_at_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the key with given value.
        - If key exists: update value and mark as MRU.
        - If key is new: insert as MRU. If capacity exceeded, evict LRU.
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value  # update value
            # Move to MRU
            self._remove(node)
            self._insert_at_front(node)
        else:
            # Create a new node and insert at MRU
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_at_front(new_node)

            # If over capacity, evict LRU (node just before tail)
            if len(self.cache) > self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
        
