
def search_rotated_array(nums, target):
   left = 0
   right = len(nums) - 1
   while (left <= right): 
      mid = (left + right) // 2
      if (nums[mid] == target):
         return mid
      if nums[left] > target:
         left = mid + 1
         continue
      elif (nums[right] > target):
         right = mid - 1
         continue
      if( nums[mid] < target and target <= nums[right]):
         left = mid + 1
      else:
         right = mid - 1
   return -1

print(search_rotated_array( [4, 5, 6, 7, 0, 1, 2],4))
print(search_rotated_array( [4, 5, 6, 7, 0, 1, 2],6))
print(search_rotated_array( [4, 5, 6, 7, 0, 1, 2],2))
print(search_rotated_array( [4, 5, 6, 7, 0, 1, 2],0))
