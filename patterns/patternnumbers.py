class Solution:
    def pattern1(self, n):
      for i in range (1 , n +1 ,1):
         for j in range(1 , n +1 , 1):
            print ( i, end ='')
         print ("")

object = Solution()
object.pattern1(5)