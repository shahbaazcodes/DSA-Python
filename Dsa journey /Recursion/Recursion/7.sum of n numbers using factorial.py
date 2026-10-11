class solution:
    def fact(self,n):
        if n == 0 or n==1:
            return 1

        return n * self.fact(n - 1)



n=3
obj = solution()
print(obj.fact(n))