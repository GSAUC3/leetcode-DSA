def majorityElement( nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    return candidate


# print(majorityElement([7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]))
nums = [7,7,5,7,5,1,5,7,5,5,7,7,7,7,5,5]
print(majorityElement(nums))
from collections import Counter
print(Counter(nums))