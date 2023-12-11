# we have to find the sum of two list indices that gives t

# class Solution:

#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         for i in range (len(nums)-1):

#             for j in range (i+1,len(nums)):

#                 if nums[i] + nums[j]==target:

#                     return ([i,j])


# class Solution:

#     def removeDuplicates(self, nums: List[int]) -> int:

#         l=1

#         for r in range(1,len(nums)):

#             if nums[r]!=nums[r-1]:

#                 nums[l]=nums[r]

#                 l+=1

#         return l
# nums[1,1,2,3,3,4,5]      
# removeDuplicates(nums)


i=1
j=2
print([i,j])