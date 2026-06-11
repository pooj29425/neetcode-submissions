class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
   
        seen=[]
        for i in nums:
            if i not in seen:
                seen.append(i)
        if len(seen)!=len(nums):
            return True
        else:
            return False



