'''Word Search II - Problem Explanation
Problem Summary
You need to find all words from a given list that can be formed by traversing a 2D board. Each cell can only be visited once per word, and you can only move horizontally or vertically to adjacent cells.

Why This is Tricky
Brute force approach: Check each word individually with DFS → O(words × board_area) which is slow
Better approach: Use a Trie to efficiently search for all words simultaneously while exploring the board
Key Insight: Trie + DFS
Instead of searching for each word separately, build a Trie of all words. Then, as you traverse the board with DFS, you can:

Prune paths early if they don't match any word prefix
Find multiple words during a single traversal
Remove words from the Trie as you find them (optimization to avoid revisiting)
Fully Commented Solution
from typing import List
'''
class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character to next TrieNode
        self.isWord = False      # True if this node marks end of a word
        self.refs = 0            # Reference count: how many words use this node

    def addWord(self, word):
        """Insert a word into the Trie"""
        cur = self
        cur.refs += 1  # Root gets a reference
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1  # Each node on path gets a reference
        
        cur.isWord = True  # Mark the end of this word

    def removeWord(self, word):
        """Remove a word from the Trie (optimization to avoid redundant searches)"""
        cur = self
        cur.refs -= 1
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie with all words
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()           # Store found words (set to avoid duplicates)
        visit = set()         # Track visited cells in current DFS path
        
        def dfs(r, c, node, word):
            """
            Explore board starting from position (r, c)
            node: current position in the Trie
            word: current word being formed
            """
            # Boundary check
            if r not in range(ROWS) or c not in range(COLS):
                return
            
            # Get current board character
            char = board[r][c]
            
            # Prune if:
            # - character not in Trie children (no word with this prefix)
            # - node refs < 1 (word already found/removed)
            # - cell already visited in this path
            if (char not in node.children 
                or node.children[char].refs < 1 
                or (r, c) in visit):
                return
            
            # Mark cell as visited
            visit.add((r, c))
            
            # Move to next Trie node
            node = node.children[char]
            word += char
            
            # If we've formed a complete word, add to result
            if node.isWord:
                node.isWord = False  # Mark as found to avoid duplicates
                res.add(word)
                root.removeWord(word)  # Remove from Trie (optimization)
            
            # Explore all 4 directions
            dfs(r + 1, c, node, word)  # Down
            dfs(r - 1, c, node, word)  # Up
            dfs(r, c + 1, node, word)  # Right
            dfs(r, c - 1, node, word)  # Left
            
            # Backtrack: unmark cell for other paths
            visit.remove((r, c))
        
        # Step 2: Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
'''
Complexity Analysis
Time: O(N × M × 4^L) worst case, where N×M is board size, L is max word length. The Trie pruning makes this much better in practice.
Space: O(W × L) for the Trie, where W is number of words and L is avg word length.
The key optimization is the refs counter—once a word is found, its nodes have refs < 1, so we never explore those dead-end paths again!
'''
        