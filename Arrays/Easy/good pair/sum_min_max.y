class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_n=-1000000
        min_n=10000000

        for i in A:
            if i> max_n:
                max_n=i
            if i<min_n:
                min_n=i
        return(max_n+min_n)

#Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

#NOTE: You should make minimum number of comparisons.
