# code to for power set - but generating only unique subsets without using a set to store unique subsets

# normal code: with set

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        n = len(nums)
        def helper(i, temp):
            res.add(tuple(temp))  
            if i >= n:
                return 
            temp.append(nums[i])
            helper(i + 1, temp)
            temp.pop()
            helper(i + 1, temp)
        
        helper(0, [])
        return [list(subset) for subset in res]


# without set 


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort to handle duplicates
        res = []
        n = len(nums)
        
        def helper(i, temp):
            res.append(temp[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue  # skip duplicate elements
                temp.append(nums[j])
                helper(j + 1, temp)
                temp.pop()
        
        helper(0, [])
        return res
