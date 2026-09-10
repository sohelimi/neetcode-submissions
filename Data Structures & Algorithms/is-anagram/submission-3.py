'''class Solution:
    def isAnagram(self, src: str, tgt: str) -> bool:
        #if length is different then no need to chk
        if len(src) != len(tgt):
            return False
        return sorted(src) == sorted(tgt)
'''
'''
class Solution:
    def isAnagram(self, src: str, tgt: str) -> bool:
        #if length is different then no need to chk
        if len(src) != len(tgt):
            return False
        return Counter(src) == Counter(tgt)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # 26 counters for a-z (only works if input is lowercase ASCII)
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1   # increment for s
        for c in t:
            count[ord(c) - ord('a')] -= 1   # decrement for t

        # All zeros means identical frequencies
        return all(x == 0 for x in count)

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
            print(c)
        print(count)
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True

#Time: O(n)
#Space: O(1) (since alphabet size is fixed)
'''