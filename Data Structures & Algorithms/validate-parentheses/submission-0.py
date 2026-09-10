class Solution:
    def isValid(self, s: str) -> bool:

        # Hash Mapping of closing brackets to their corresponding opening brackets
        match = {')': '(', ']': '[', '}': '{'} #First and last braket is for hash syntex
        stack = []  # Stack to keep track of opening brackets
        '''
        for char in s:
            if char not in match:
                stack.append(char)
            else:
                if not stack or stack[-1] !=match[char]:
                    return False
                stack.pop()
        return not stack
        '''
        for char in s:
            # If it's an opening bracket, push onto stack
            if char not in match:
                stack.append(char)
            else:
                # If no opening bracket to match or mismatch, string is invalid
                if not stack or stack[-1] != match[char]:
                    return False
                # Match found, pop the opening bracket
                stack.pop()

        # If stack is empty, all brackets matched correctly
        return not stack