Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that
 a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must 
 not be duplicates.

Example:
```
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
```
Here's a starting point:
```
class Solution(object):
  def threeSum(self, nums):
    # Fill this in.

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
```


## Solution

- [Python Solution](./Solution.py)