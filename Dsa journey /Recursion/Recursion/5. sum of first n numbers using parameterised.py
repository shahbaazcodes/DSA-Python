class solution:
    def function(self,i,s):
        if i<1:
            print(s)
            return

        self.function(i-1,s+i)
        

n=5
obj=solution()
obj.function(n,0)