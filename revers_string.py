class Solution:
  def reverseString(self, s):
    return s[::-1]
  def reverseFunc(self,s):
    return ''.join(reversed(s))
  def reverseWord(self,s):
    reversed_string = ''
    for letter in s:
      reversed_string = letter + reversed_string
    return reversed_string
    



s =Solution()
print(s.reverseString('sandeep is my name'))
print(s.reverseFunc('sandeep is my name'))
print(s.reverseWord('sandeep'))
