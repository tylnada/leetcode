#Brutal Force O(N^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = float("-inf")
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums+1):
                if nums[i] > max_num:
                        max_num = nums[i]
                else:
                    if sum(nums[i:j]) > max_num:
                        max_num = sum(nums[i:j])
        return max_num
      
#Better readability O(N^2):
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = float("-inf")
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums+1):
                if nums[i] > max_num:
                        max_num = nums[i]
                else:
                    if sum(nums[i:j]) > max_num:
                        max_num = sum(nums[i:j])
        return max_num

#Dynamic Programming, Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
