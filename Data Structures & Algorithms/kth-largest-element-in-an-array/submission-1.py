class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums) - 1
        pivot = nums[0]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
            
        nums[i] = pivot

        if len(nums) - i == k:
            return nums[i]
        if len(nums) - i < k:
            return self.findKthLargest(nums[:i], k - (len(nums) - i))
        if len(nums) - i > k:
            return self.findKthLargest(nums[i+1:], k)
