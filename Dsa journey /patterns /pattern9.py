class Solution:
    def pyramid(self, n):
        for i in range(1 , n+1,1):
            for j in range(1,n-i+1+1, 1):
                print(" ",end='')

            for j in range(1,i+i,1):
                print("*",end='')
            print()

        for i in range(1 , n+1,1):
            for j in range(1,i+1, 1):
                print(" ",end='')

            for j in range(1,n-i+n-i+1+1,1):
                print("*",end='')
            print()
            
        
object = Solution()
object.pyramid(5)