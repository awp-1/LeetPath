class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                if k >= i - hashmap[nums[i]]:
                    return True
            hashmap[nums[i]] = i
        return False