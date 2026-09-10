from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            #print(seen)
            complement = target - nums[i]
            if complement in seen:
                return[seen[complement],i] #The returned values are the indexes, not the numbers themselves.
            seen[num] = i

'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store numbers we've seen and their indices, initiall set to empty
        seen = {}
        print("Seen1: ", seen)
        #enumerate through the list
        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i] #Then return key for the complement and i
            seen[num] = i #else put the key, value to the hash map or dict

        print("Seen2: ", seen)


'''
       

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store numbers we've seen and their indices
        seen1 = {}
        
        # Iterate through each number in the array with its index
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num

            # Check if we've already seen the complement
            if complement in seen1:
                # Found the pair! Return indices (smaller index first)
                return [seen1[complement], i]
            
            # Store current number and its index in the hashmap
            seen1[num] = i
        
        # Return empty list if no solution found (though problem guarantees one exists)
        return []

'''

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
