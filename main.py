"""
Given a sorted integer array nums and two integers—k and num—return the k closest integers to num in this array. Ensure that the result is sorted in ascending order.

The integer a is closer to num than an integer b if the following are true:
"""


def find_closest_elements(nums, k, num):
  # find num in nums
  # not guaranteed to find it, handle this case
  closest_num = find_elem(nums, num)
  # Case 1: can go left and right
  # Case 2: only right
  # Case 3: only left
  left, right = closest_num, closest_num
  # left, right = max(0,closest_num - 1), min(closest_num + 1, len(nums)-1)
  # result = [nums[closest_num]]
  # left_elem, right_elem = 10**6, 10**6
  # total_elems = 0
  print(left, right)
  while (right - left) + 1 < k:
    if left -1 >= 0:
      # can still go left
      if right + 1 < len(nums):
        # can also go right
        # compare left and right and decide
        if (abs(num - nums[left-1]) <= abs(num - nums[right+1])):
          left -=1
        else:
          #print("went right: bcoz right is closer")
          #print(nums[left-1], nums[right+1])
          right +=1
      else:
        # can not go right
        left -=1
    else:
      # can only go right
      print("went right: can only go right")
      right +=1
    print(left, right)
  return nums[left:right + 1]


# [1,22,33,44], 33 = 2
# [1,22,33,44], 35 = 2
# [1,22,33,44], 39 = 3
def find_elem(nums, num):
  lo, hi = 0, len(nums) - 1
  closest_num, closest_idx = (10**6), -1
  while lo <= hi:
    mid = lo + int((hi - lo) // 2)

    if nums[mid] == num:
      return mid
    if num > nums[mid]:
      lo = mid + 1
    else:
      hi = mid - 1
    # setting closest
    if abs(nums[mid] - num) < abs(closest_num - num):
      #print("Found closer num", nums[mid])
      closest_num, closest_idx = nums[mid], mid
    #print(lo, hi, mid)
  return closest_idx


# print(find_elem([1,22,33,44], 33))
#print(find_closest_elements([1, 22, 33, 44], 2, 35))
#print(find_closest_elements([1, 22, 33, 44], 3, 35))
#print(find_closest_elements([1, 22, 33, 44], 3, 39))
#print(find_closest_elements([1,22,33,44], 4, 700))
# print(find_closest_elements([-29, -11, -3, 0, 5, 10, 50, 63, 198] , 6 , 8))
"""
Learnings: 
- Binary Search: while lo <= hi, hi = mid + 1, lo = mid -1, otherwise loops do not terminante 
- return closest number if cannot find number in binary search
- Find a pivot point and expand outwards, handle complex logic with being in bounds in arrays
- When you have a bunch of complex conditions useful to reason about it in if conditions. Can still go left, Can still go right etc 
"""
