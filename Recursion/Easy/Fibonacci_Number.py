class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
 

        elif n == 1 or n == 2:
            return 1
 
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        
n = int(input())

s1 = Solution()
print(s1.fib(n))