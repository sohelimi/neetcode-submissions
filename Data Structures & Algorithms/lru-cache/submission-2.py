class Node:
    """A node in a doubly linked list holding a cache entry."""
    def __init__(self, key, value):
        self.key = key      # needed so we can delete from the dict on eviction
        self.value = value
        self.prev = None    # link to the previous (more recently used) node
        self.next = None    # link to the next (less recently used) node


class LRUCache:
    """
    LRU (Least Recently Used) Cache.

    Design:
      - A hash map (dict)   : key -> Node   → O(1) lookup
      - A doubly linked list: tracks usage order → O(1) move / remove

    Ordering convention (chosen arbitrarily, but must stay consistent):
        head <-> [most recently used] <-> ... <-> [least recently used] <-> tail
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                     # key -> Node

        # Two sentinel (dummy) nodes. They are never removed and hold no
        # real data. They remove all "empty list" edge cases from the
        # insert / remove logic.
        self.head = Node(0, 0)              # MRU side
        self.tail = Node(0, 0)              # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # ------------------------------------------------------------------
    # Internal helpers: operate directly on the linked list (no dict)
    # ------------------------------------------------------------------

    def _remove(self, node: Node) -> None:
        """Unlink `node` from the doubly linked list. O(1)."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        # (Optionally: node.prev = node.next = None  — not required)

    def _insert_at_front(self, node: Node) -> None:
        """Insert `node` right after head, i.e. mark it as most recently used. O(1)."""
        first = self.head.next   # current MRU node
        # Wire head <-> node
        self.head.next = node
        node.prev = self.head
        # Wire node <-> first
        node.next = first
        first.prev = node

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get(self, key: int) -> int:
        """
        Return the value of `key` if present, else -1.
        Accessing a key marks it as most recently used.
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move node to the MRU position.
        self._remove(node)
        self._insert_at_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update `key`. If inserting pushes us over capacity,
        evict the least recently used entry.
        """
        if key in self.cache:
            # ----- Update existing entry -----
            node = self.cache[key]
            node.value = value          # update the value in place
            self._remove(node)          # take it out of its old position
            self._insert_at_front(node) # ...and move it to MRU
            return

        # ----- Insert new entry -----
        node = Node(key, value)
        self.cache[key] = node
        self._insert_at_front(node)

        # Evict if over capacity.
        if len(self.cache) > self.cap:
            lru = self.tail.prev        # node just before tail = least recently used
            self._remove(lru)           # unlink from list
            del self.cache[lru.key]     # remove from map (that's why Node stores key!)
'''
Quick usage check
lru = LRUCache(2)
lru.put(1, 10)     # cache: {1=10}
lru.get(1)         # -> 10      (1 becomes MRU)
lru.put(2, 20)     # cache: {1=10, 2=20}
lru.put(3, 30)     # cache: {2=20, 3=30}  — key 1 evicted
lru.get(2)         # -> 20
lru.get(1)         # -> -1
Why each piece exists
Node.key Needed at eviction time to del self.cache[lru.key]. Without it, we'd only have the node, not the map key. Sentinels head/tail Guarantee node.prev / node.next always exist → _remove and _insert_at_front need zero edge-case branches. _remove + _insert_at_front The only two list mutations. Reused by get, update-put, and insert-put. Dict stores Node, not just value So get/put can jump straight to the list node and reorder in O(1).
Complexity
Time: get → O(1), put → O(1)
Space: O(capacity) — at most cap + 1 nodes (the +1 exists only momentarily before eviction), plus cap dict entries.

'''



