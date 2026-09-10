class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string containing only alphanumeric characters.
        #
        # char.isalnum() keeps letters and digits.
        # Characters such as spaces, commas, and question marks are removed.
        #
        # .lower() makes the comparison case-insensitive.
        #
        # Example:
        # "Was it a car?" becomes "wasitacar"
        sCleaned = "".join(
            char for char in s
            if char.isalnum()
        ).lower()

        # This prints the cleaned string for debugging.
        # It should be removed when submitting the solution.
        # print(sCleaned)

        # lpos starts at the first character.
        # rpos starts at the last character.
        lpos = 0
        rpos = len(sCleaned) - 1

        # Continue comparing while the pointers have not crossed.
        #
        # When lpos == rpos, there is only one middle character,
        # which always matches itself, so no comparison is needed.
        while lpos < rpos:

            # These prints are also only for debugging.
            # They show the pair of characters currently being compared.
            # print(sCleaned[lpos], sCleaned[rpos])

            # If the characters from opposite ends differ,
            # the string is not a palindrome.
            if sCleaned[lpos] != sCleaned[rpos]:
                return False

            # Move both pointers toward the center.
            lpos += 1
            rpos -= 1

        # Every pair matched, so the string is a palindrome.
        return True
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                # If they don't match, it's not a palindrome
                return False

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If all characters matched, it's a palindrome
        return True
'''
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
'''
