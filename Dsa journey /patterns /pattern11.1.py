class Solution:
    def pyramid(self, n):
        for i in range(1 , n+1,1):
            for j in range(1,n-i+1, 1):
                print(" ",end='')
        
           
            x=i
            for j in range(1,i+1,1):
                print( x,end='')
                x = x-1
                
            y =2
            for j in range(1, i, 1):
                print( y,end = '')
                y = y+1
            print()
            
        
object = Solution()
object.pyramid(5)