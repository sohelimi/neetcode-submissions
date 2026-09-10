class Solution:
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

