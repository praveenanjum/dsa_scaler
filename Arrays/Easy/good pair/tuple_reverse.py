class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        a=[]
        n=len(A)
        for i in range (n-1,-1,-1):
            a.append(A[i])
        return(a)
# tuple cannot be changed so we create a new list and append the elements of tuple in reverse order and return the list