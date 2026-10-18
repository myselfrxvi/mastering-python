from typing import List
def remove_duplicates(nums: List[int]) -> None:
    if not nums: 
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

print("Hello World")
arr = [0,0,1,1,1,2,2,3,3,4]
remove_duplicates(arr)
print(arr)