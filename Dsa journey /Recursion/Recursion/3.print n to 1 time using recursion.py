class Solution:
    def function(self,i,n):
        if i < 1:
            return 
        print(i)
        self.function(i-1,n)

    
        

obj = Solution()

obj.function(5,5)