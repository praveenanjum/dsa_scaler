class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c=0
        A.sort()
        n=len(A)
        for i in range(0,n):
            for j in range (i+1,n):
                if A[i]!=A[j]:
                    c=c+1
            if c==A[i]:
                return (1)
            else:
                c=0
        return(-1)
