class Solution:
    def function(self,i):
        if i < 1:
            return 
        print(i)
        self.function(i-1)

    
        

obj = Solution()

obj.function(5)