def majority_element(nums):
    # Phase 1: Find candidate
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Phase 2: Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None  # No majority element

