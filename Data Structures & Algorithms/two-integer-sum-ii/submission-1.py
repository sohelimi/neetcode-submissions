'''class Solution:
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
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: left at the start, right at the end
        left, right = 0, len(numbers) - 1

        # Because the array is sorted, we can adjust pointers to reach the target sum
        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If we found the target sum
            if current_sum == target:
                # Return 1-indexed positions as required
                return [left + 1, right + 1]

            # If the sum is too large, move the right pointer left to decrease sum
            elif current_sum > target:
                right -= 1

            # If the sum is too small, move the left pointer right to increase sum
            else:
                left += 1

        # The problem guarantees exactly one solution, so we won't reach here in valid inputs.
        # Returning an empty list here for safety.
        return []
