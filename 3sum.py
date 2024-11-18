from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    i = 0
    nums.sort()

    while (i < len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        
        while (l < r):
            sm = nums[i] + nums[l] + nums[r]
            
            if(sm == 0):
                res.append([nums[i], nums[l], nums[r]])
                
                while (l < r) and nums[l] == nums[l+1]:
                    l += 1
                
                while (l < r) and nums[r] == nums[r-1]:
                    r -= 1
                
                l += 1
                r -= 1 
            
            elif(sm < 0):
                l += 1

            else: r -= 1

        while (i < len(nums) - 2) and nums[i] == nums[i+1]:
            i += 1
        i += 1
    
    return res

testNums = [-1,0,1,2,-1,-4]
print (threeSum(testNums))
        
