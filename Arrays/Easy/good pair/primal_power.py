class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c=0
        
        for i in range (0,len(A)):
            prime=1
            if A[i]>1:
                for j in range (2,A[i]):
                    #print(A[i],j)
                    if A[i]%j==0:
                        #print("insdie")
                        prime=0
                        # break
                if prime ==1:
                    c=c+1
            if A[i]==1 or A[i]==0:
                prime=0

        return(c)
#TLE revisit this problem!
