class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        size=len(A)
        max_num=A[size-1]
        leaders=[]
        leaders.append(A[size-1])
        for i in range (size-2,-1,-1):
            if A[i]>max_num:
                max_num=A[i]
                leaders.append(A[i])

        return(leaders)
