'''Prefix Tree (Trie) Explanation
Problem Overview
You need to implement a Trie, a tree data structure that stores strings efficiently. Each node represents a character, and paths from root to leaf form words.

Key Operations:

insert(word) - Add a word to the trie
search(word) - Check if exact word exists
startsWith(prefix) - Check if any word starts with given prefix
How It Works
Imagine storing words "dog", "do", "cat":

       root
      /    \
     d      c
     |      |
     o      a
    / \     |
   g   (word end)  t
 (word end)    (word end)
Each node has 26 children (for 'a'-'z')
Each node tracks if it's an end of a word (boolean flag)
search requires both: path exists AND node marked as word end
startsWith only needs: path exists (doesn't check word end flag)
Complete Code with Comments
'''

class PrefixTreeNode:
    def __init__(self):
        # Array of 26 pointers for each lowercase letter a-z
        self.children = [None] * 26
        # Flag to mark if this node represents the end of a valid word
        self.end = False

class PrefixTree:
    def __init__(self):
        # Initialize root node (empty starting point)
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        Time: O(m) where m is length of word
        Space: O(m) for new nodes
        """
        curr = self.root
        # Traverse/build path for each character
        for c in word:
            # Convert character to index: 'a'->0, 'b'->1, ..., 'z'->25
            i = ord(c) - ord("a")
            # Create new node if path doesn't exist
            if curr.children[i] is None:
                curr.children[i] = PrefixTreeNode()
            # Move to next node
            curr = curr.children[i]
        # Mark the final node as end of a valid word
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Search for exact word in trie.
        Returns True only if word exists AND is marked as complete word.
        Time: O(m) where m is length of word
        Space: O(1)
        """
        curr = self.root
        # Traverse the path character by character
        for c in word:
            i = ord(c) - ord("a")
            # Path doesn't exist
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        # Return whether this node marks end of a word
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word in trie starts with given prefix.
        Returns True if path exists (regardless of word end flag).
        Time: O(m) where m is length of prefix
        Space: O(1)
        """
        curr = self.root
        # Traverse the path for prefix
        for c in prefix:
            i = ord(c) - ord("a")
            # Path doesn't exist
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        # If we completed the prefix path, return True
        return True
    '''
Key Differences: search vs startsWith
search("do") ✓ ✓ Returns False if only "dog" inserted startsWith("do") ✓ ✗ Returns True if "dog" or "do" inserted
Complexity Analysis
Time: All operations O(m) where m = word/prefix length
Space: O(N × 26) where N = total characters in all inserted words
'''
        
        