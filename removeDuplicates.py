def removeDuplicates(nums: list[int]) -> int:
    # Handle the edge case of an empty array, although constraints say 1 <= length.
    if not nums:
        return 0
    
    # 'k' (or insertIndex) is the pointer for the next position to insert a unique element.
    # We start at 1 because nums[0] is always the first unique element.
    k = 1
    
    # 'i' is the pointer to iterate through the array, starting from the second element.
    for i in range(1, len(nums)):
        # Compare the current element (nums[i]) with the last *recorded* unique element (nums[k-1]).
        if nums[i] != nums[k - 1]:
            # Found a new unique element!
            
            # Place the new unique element at the 'k' position
            nums[k] = nums[i]
            
            # Move the 'k' pointer forward to the next empty spot
            k += 1
            
    # k is the number of unique elements and the length of the new sub-array.
    return k

# Example 1 Test:
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(f"Example 1: k = {k1}, nums = {nums1[:k1]}")
# Expected: k = 2, nums = [1, 2]

# Example 2 Test:
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(f"Example 2: k = {k2}, nums = {nums2[:k2]}")
# Expected: k = 5, nums = [0, 1, 2, 3, 4]