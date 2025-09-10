class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res=[]
        for i in range (0,len(A)):
            if i==0 and len(A)==1:
                res.append(A[i])
                #print(res)
            elif i ==0 and len(A)!=1:
                res.append(A[i]*A[i+1])
                #print(res)
            elif i==(len(A)-1) and len(A)!=1:
                res.append(A[i]*A[i-1])
                #print(res)
            else:
                res.append(A[i-1]*A[i+1])
                #print(res)
        return (res)