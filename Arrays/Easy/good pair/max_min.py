class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n=len(A)
        # print(A)
        return(A[n-B]-A[B-1])
