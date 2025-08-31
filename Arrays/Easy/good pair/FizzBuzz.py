class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
            
            list1=[]
            for i in range (1,A+1):
                if i %3 ==0 and i %5==0:
                    list1.append('fizzBuzz')
                elif i%3==0:
                    list1.append('Fizz')
                elif (i%5==0):
                    list1.append('Buzz')
                else:
                    list1.append(i)
            return (list1)