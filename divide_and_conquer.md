## 215. Kth Largest Element in an Array

>> Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
>> For example,
>> Given [3,2,1,5,6,4] and k = 2, return 5.

- 思路：通过快排的思路，将原数组一分为二(小，key，大)
  - 如果len(nums)-key.index = k, 当前key就是第k大的值，
  - 如果len(nums)-key.index > k, 说明第k大的值在key后面
  - 如果len(nums)-key.index < k, 说明第k大的值在key前面
  
  ```python
  class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            index = self.partition(nums, low, high)
            if len(nums)-index > k:
                low = index + 1
            elif len(nums) - index < k:
                high = index - 1
            else:
                break
        return nums[len(nums) - k]
                
        
        
    def partition(self, nums, low, high):
        if low >= high:
            return high
        pivot = nums[low] # 以nums[low]当作pivot
        i = low
        j = high
        
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
            while i < j and nums[i] < pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        return i
 ```
