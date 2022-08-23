class Solution:
    def fib(self, n: int) -> int:
        
        fibolist = [0, 1]
        while len(fibolist) <= n:
            fibolist.append(fibolist[-1] + fibolist[-2])
            
        return fibolist[n]