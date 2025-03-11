# Write a function thant takes a list of integers as a parameters andd 
# returns third smallest number from the list. For example, 
# input:[34,89,54,20,50,76,10,45,90] output: 34 

def third_smallest(nums):
    for i in range(0,3):
        smallest_indx=i
        for j in range(i+1,len(nums)):
            if nums[smallest_indx]>nums[j]:
                smallest_indx=j
        nums[i],nums[smallest_indx]=nums[smallest_indx],nums[i]
    return nums[2]


nums = [4, 2, 4, 10,100,5,1]
print(third_smallest(nums))
