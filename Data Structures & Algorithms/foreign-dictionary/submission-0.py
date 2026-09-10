'''Alien Dictionary Problem Explanation
This is a graph problem that requires you to deduce the ordering of characters in an alien language based on sorted words.

Key Insight
When two consecutive words differ at position j, the character at w1[j] must come before w2[j] in the alien alphabet. We can represent this as a directed graph and perform a topological sort.

Step-by-Step Approach
Build the graph: Compare consecutive words to find character ordering relationships
Validate: Check for invalid cases (e.g., longer word comes before its prefix)
Topological Sort: Use DFS to order characters while detecting cycles (contradictions)
Edge Cases to Handle
Invalid prefix case: If "abc" comes before "ab", return "" (impossible ordering)
Cycles: If characters form a cycle (e.g., a→b→c→a), return ""
Commented Solution
'''
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize adjacency list with all unique characters
        adj = {char: set() for word in words for char in word}
        
        # Build the graph by comparing consecutive words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # Invalid case: w1 is longer and is a prefix of w2
            # e.g., "abc" before "ab" is impossible
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Find first differing character and add edge to graph
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # w1[j] comes before w2[j] in alien alphabet
                    adj[w1[j]].add(w2[j])
                    break
        
        # Perform DFS-based topological sort to detect cycles
        # visited: 0 = unvisited, 1 = visiting (current path), -1 = visited
        visited = {}  # {char: bool}
        res = []
        
        def dfs(char):
            # If already visited in current path, we have a cycle
            if char in visited:
                return visited[char]
            
            # Mark as visiting (True = currently in path)
            visited[char] = True
            
            # Visit all neighbors
            for neighbor in adj[char]:
                # If neighbor returns True, cycle detected
                if dfs(neighbor):
                    return True
            
            # Mark as fully visited (False = done processing)
            visited[char] = False
            # Add to result in reverse topological order
            res.append(char)
            
            return False
        
        # Run DFS on all characters
        for char in adj:
            # If cycle detected, return empty string
            if dfs(char):
                return ""
        
        # Reverse to get correct topological order
        res.reverse()
        return "".join(res)
'''
Complexity Analysis
Time: O(N × L + U + V + E) where N = number of words, L = average word length, U = unique characters, V = vertices in graph, E = edges
Space: O(U) for adjacency list and visited set
Example Walkthrough
For ["hrn","hrf","er","enn","rfnn"]:

Compare "hrn" and "hrf" → n → f
Compare "hrf" and "er" → h → e
Compare "er" and "enn" → r → n
Compare "enn" and "rfnn" → e → r
Graph edges: h→e→r→n→f

DFS processes in reverse order to produce: "hernf" ✓'''