#brute force approach 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min_avg=1000000000
        first_element_index=0
        for i in range (0,len(A)):
            k=i+B
            if k<=len(A):
                s=0
                for j in range (i,k):
                    s= s+A[j]
                avg=s/B
                #print(avg)
                if min_avg>avg:
                    min_avg=avg
                    first_element_index=i
        return(first_element_index)


