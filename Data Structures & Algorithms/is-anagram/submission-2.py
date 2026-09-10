'''class Solution:
    def isAnagram(self, src: str, tgt: str) -> bool:
        #if length is different then no need to chk
        if len(src) != len(tgt):
            return False
        return sorted(src) == sorted(tgt)
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