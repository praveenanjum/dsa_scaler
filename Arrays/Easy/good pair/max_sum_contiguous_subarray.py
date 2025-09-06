class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        s=0
        max_sum=-1000000
        for i in range (0,len(A)):
            s=s+A[i]
            if s>max_sum:
                max_sum=s
            if s<0:
                s=0
        return (max_sum)