class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to the opening bracket it requires.
        #
        # For example:
        # ')' must match '('
        # ']' must match '['
        # '}' must match '{'
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # The stack stores opening brackets that have not been closed yet.
        stack = []

        # Process each character from left to right.
        for char in s:

            # If char is not a key in match, it is an opening bracket.
            #
            # For example:
            # '(' is not in match, so push it onto the stack.
            # '[' is not in match, so push it onto the stack.
            if char not in match:
                stack.append(char)

            else:
                # char is a closing bracket.
                #
                # There are two invalid cases:
                #
                # 1. The stack is empty:
                #    There is no opening bracket to match this closing bracket.
                #
                # 2. The top of the stack is not the correct opening bracket.
                #
                # The top of the stack is stack[-1] because brackets must
                # close in reverse order of how they were opened.
                if not stack or stack[-1] != match[char]:
                    return False

                # The closing bracket correctly matches the opening bracket
                # at the top of the stack, so remove that opening bracket.
                stack.pop()

        # If the stack is empty, every opening bracket was matched.
        #
        # If the stack is not empty, some opening brackets were never closed.
        return not stack