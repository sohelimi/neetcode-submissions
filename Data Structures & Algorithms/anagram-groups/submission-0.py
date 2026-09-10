class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a list of strings into anagrams using the sorted string as the key.

        Args:
            strs (List[str]): The input list of strings.

        Returns:
            List[List[str]]: Groups of anagrams, each group as a list.
        """
        # Create a dictionary that maps the sorted string to the list of original words.
        # defaultdict(list) automatically initializes empty lists for new keys.
        groups: dict[str, List[str]] = defaultdict(list)

        for word in strs:
            # Sort the characters of each word to create the canonical key.
            # Example: "eat" -> "aet", "tea" -> "aet"
            key = ''.join(sorted(word))
            # Add the word to the group corresponding to its sorted key.
            groups[key].append(word)

        # Return all the groups of anagrams as a list of lists.
        return list(groups.values())