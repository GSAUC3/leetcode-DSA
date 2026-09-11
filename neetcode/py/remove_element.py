
nums = [0,1,2,2,3,0,4,2] 
val = 2
from collections import Counter

valptr = 0
nonvalptr = len(nums) -1

while valptr < nonvalptr:
    print(valptr, nonvalptr, nums)
    while nums[valptr]!=val and valptr<len(nums):
        valptr+=1
    
    while nums[nonvalptr]==val and nonvalptr>0:
        nonvalptr-=1
    

    if nums[valptr]==val and nums[nonvalptr]!=val and valptr<nonvalptr:
        nums[valptr], nums[nonvalptr] = nums[nonvalptr], nums[valptr]

print(nums)
print(len(nums) - Counter(nums)[val])