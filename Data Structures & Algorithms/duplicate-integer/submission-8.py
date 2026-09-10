from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]):
        unq = set(nums)
        count = Counter(nums)

        for key, val in count.items():
            if val > 1:
                return True
        return False 



















'''from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False
'''
'''
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]):
        myset = set(nums)
        count = Counter(nums)
        for key, val in count.items():
            if val > 1 :
                return True
        return False
        #print(count)
'''

'''


from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#Time: O(n)
#Space: O(n)
'''