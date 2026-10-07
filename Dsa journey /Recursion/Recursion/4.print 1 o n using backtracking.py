class Solution:
    def function(self,i,n):
        if i < 1:
            return
        self.function(i-1,n)
        print(i)



obj = Solution()
obj.function(5,5)
