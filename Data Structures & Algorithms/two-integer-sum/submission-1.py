from typing import List

'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        retn = []

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    retn.append(i)
                    retn.append(j)
                    return retn
        return retn
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashmap
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
        return[]

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

'''
