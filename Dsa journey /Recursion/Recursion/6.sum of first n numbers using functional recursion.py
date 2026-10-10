class solution:
    def funciton(self,n):
        if n == 0:
            return 0

        return n + self.funciton(n-1)


obj = solution()
print(obj.function(3))