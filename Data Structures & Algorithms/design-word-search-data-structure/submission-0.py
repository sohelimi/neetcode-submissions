class WordDictionary:

    def __init__(self):
        # Root of Trie (empty dictionary)
        self.root = {}

    def addWord(self, word: str) -> None:
        # Start from root
        node = self.root
        
        # Traverse each character in the word
        for ch in word:
            
            # If character not present, create new dictionary
            if ch not in node:
                node[ch] = {}
            
            # Move to next level
            node = node[ch]
        
        # Mark end of word using special key
        node["#"] = True   # '#' indicates end of word

    def search(self, word: str) -> bool:
        
        # DFS helper function
        def dfs(node, i):
            # node = current dictionary (Trie node)
            # i = index in word
            
            # If we reached end of word
            if i == len(word):
                # Check if end-of-word marker exists
                return "#" in node
            
            ch = word[i]
            
            # If character is not wildcard
            if ch != ".":
                
                # If character not found → False
                if ch not in node:
                    return False
                
                # Move to next node
                return dfs(node[ch], i + 1)
            
            else:
                # If '.' → try all possible children
                
                for key in node:
                    
                    # Skip end marker
                    if key == "#":
                        continue
                    
                    # Try each child
                    if dfs(node[key], i + 1):
                        return True
                
                # If none worked
                return False
        
        # Start DFS from root
        return dfs(self.root, 0)
        
