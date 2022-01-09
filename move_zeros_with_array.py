#move all the zeros in array toward the end of array
#final array should be created
#check the given array
#check for non zero values
#start adding non zeros values in the array with index
#get the len of array and add zeros for the range between the 
#number of non zeros and lengh of array

class Solution:
  def moveZeros(self, nums):
    #check for non zero
    new_array =[]
    counter =0 
    for num in nums:
      if num != 0:
        new_array.append(num)
        counter += 1
    for index in range(counter, len(nums)):
      new_array.append(0)
    print(new_array)

s = Solution()
l=[0,0,0,1,0,2,0,4,1]
print(l)
s.moveZeros(l)
        
