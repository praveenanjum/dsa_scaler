# Brute Force Approach O(n^2); find each pair and check if sum is equal to B
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range (0,len(A)):
            for j in range (1,len(A)):
                if i!=j:
                    if A[i]+A[j]==B:
                        return('1')
        return('0')
    
# Optimal Approach O(n) using Hashing
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        list1=[]
        for i in range (0,len(A)):
            add_num =B-A[i]
            if add_num in list1:
                return ('1')    
            else:
                list1.append(A[i])
        return('0')