class Solution:
  def missingNumber(self, nums):
    # length of array
    l = len(nums)
    #1 sum of length of array with n*(n+1)/2
    intendedsum = l*(l+1)/2
    #2 sum of each iteam in array
    # 1-2 to get the missing number
    val = 0
    for num in nums:
      val = val + num

    curSum= sum(nums)
    missingNum=(intendedsum - val)
    print(missingNum)


s = Solution()
s.missingNumber([0,1,2,3,5,6,4,9,7])
