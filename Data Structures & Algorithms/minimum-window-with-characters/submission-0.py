class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, there is no required substring.
        if not t:
            return ""

        # count_t stores how many times each character is required.
        #
        # Example:
        # t = "AABC"
        # count_t = {"A": 2, "B": 1, "C": 1}
        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # window stores character frequencies inside the current window
        # of s.
        window = {}

        # "need" is the number of unique characters from t that must
        # satisfy their required frequency.
        #
        # Example:
        # t = "AABC"
        # need = 3, because the unique characters are A, B, and C.
        need = len(count_t)

        # "have" tells us how many unique characters currently satisfy
        # their required frequency inside the window.
        have = 0

        # These variables store the best window found so far.
        best_start = 0
        best_length = float("inf")

        # Left side of the sliding window.
        left = 0

        # Expand the window by moving right through s.
        for right in range(len(s)):
            current_char = s[right]

            # Add the current character to the window.
            window[current_char] = window.get(current_char, 0) + 1

            # If this character is required and we now have exactly
            # enough copies of it, one more requirement is satisfied.
            #
            # We use == rather than >= so that extra copies do not
            # increase "have" more than once.
            if (
                current_char in count_t
                and window[current_char] == count_t[current_char]
            ):
                have += 1

            # Once all required character frequencies are satisfied,
            # try to shrink the window from the left.
            while have == need:
                current_length = right - left + 1

                # Record this window if it is smaller than the best
                # valid window found so far.
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                # Remove the leftmost character before moving left
                # forward.
                left_char = s[left]
                window[left_char] -= 1

                # If removing this character causes its count to fall
                # below the required count, the window is no longer
                # valid.
                if (
                    left_char in count_t
                    and window[left_char] < count_t[left_char]
                ):
                    have -= 1

                left += 1

        # If best_length is still infinity, no valid window exists.
        if best_length == float("inf"):
            return ""

        # Otherwise, return the smallest valid substring.
        return s[best_start : best_start + best_length]