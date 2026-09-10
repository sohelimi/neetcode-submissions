'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            #print(i)
            res = 1
            for j in range(len(nums)):
                if i != j:
                    #print(i,j)
                    res = res*nums[j]
            product.append(res)
        return product
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array answer such that answer[i] is the product
        of all the elements of nums except nums[i], without using division.
        Time: O(n), Space: O(1) (output array excluded)
        """
        n = len(nums)
        # Initialize result array where result[i] will store the final answer for index i.
        result = [1]*n

        # prefix will hold the product of all elements to the left of i.
        prefix = 1
        # First pass: Fill in prefix products.
        for i in range(n):
            result[i] = prefix # For i == 0, prefix = 1, so result[0] = 1.
            prefix *= nums[i] # Update prefix product including nums[i].   

        # suffix will hold the product of all elements to the right of i.
        suffix = 1
        # Second pass: Multiply with suffix products.
        for i in range(n-1, -1, -1):
            result[i] *= suffix # Multiply current result by the right-side product.
            suffix *= nums[i] # Update suffix product including nums[i].

        return result
        