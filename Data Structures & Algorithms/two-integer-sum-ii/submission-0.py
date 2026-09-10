class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left, right = 0, len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                res = [left + 1, right + 1]
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return res