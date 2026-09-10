class Solution:

    def encode(self, strs: List[str]) -> str:
        # For each string `s`, create a substring like "5#hello" if s == "hello".
        # Join all such substrings together to form the encoded string.
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # Current parsing index in the string 's'
        while i < len(s):
            # Find the position of the next '#' - this separates the length from the string content
            j = s.index('#', i)
            # Parse the length field (between current index and '#')
            length = int(s[i:j])
            # The string starts after '#' and spans 'length' characters
            result.append(s[j + 1 : j + 1 + length])
            # Advance the parsing index to the start of the next encoded string (if any)
            i = j + 1 + length
        return result

'''
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string using length-prefix encoding.

        For each string, output its length, a delimiter '#', then the string itself.
        This allows the decoder to know exactly where each string ends and starts, 
        even if the strings themselves contain numbers or the '#' character.

        Args:
            strs (List[str]): List of strings to encode.

        Returns:
            str: The encoded string.
        """
        # For each string `s`, create a substring like "5#hello" if s == "hello".
        # Join all such substrings together to form the encoded string.
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into a list of strings using length-prefix encoding.

        The decoder reads the length prefix, finds the delimiter '#', determines how many 
        characters to extract for each string, and repeats this until the entire input is processed.

        Args:
            s (str): The encoded string.

        Returns:
            List[str]: The list of decoded strings.
        """
        result = []
        i = 0  # Current parsing index in the string 's'
        while i < len(s):
            # Find the position of the next '#' - this separates the length from the string content
            j = s.index('#', i)
            # Parse the length field (between current index and '#')
            length = int(s[i:j])
            # The string starts after '#' and spans 'length' characters
            result.append(s[j + 1 : j + 1 + length])
            # Advance the parsing index to the start of the next encoded string (if any)
            i = j + 1 + length
        return result
'''
