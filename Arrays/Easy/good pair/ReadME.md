GOOD PAIR:
Given an array A and an integer B, good pair if i!=j and A[i]+A[j]=B return 1 else return 0

FixBuzz:
Problem Description:
Given a positive integer A, return an array of strings with all the integers from 1 to N. But for multiples of 3 the array should have “Fizz” instead of the number. For the multiples of 5, the array should have “Buzz” instead of the number. For numbers which are multiple of 3 and 5 both, the array should have "FizzBuzz" instead of the number.


Time to Equality:

Problem Description:
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Example Input

A = [2, 4, 1, 3, 2]


Example Output

8

Noble Integer:
Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.



Problem Constraints

1 <= |A| <= 2*105
-108 <= A[i] <= 108


Input Format

First and only argument is an integer array A.



Output Format

Return 1 if any such integer p is present else, return -1.



Example Input

Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


 max_sum_contiguous_subarray:

 Problem Description

Given an array A of length N, your task is to find the maximum possible sum of any non-empty contiguous subarray.

In other words, among all possible subarrays of A, determine the one that yields the highest sum and return that sum.



Problem Constraints

1 <= N <= 106
-1000 <= A[i] <= 1000



Input Format

The first and the only argument contains an integer array, A.



Output Format

Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input

Input 1:

 A = [1, 2, 3, 4, -10] 
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 


Example Output

Output 1:

 10 
Output 2:

 6 


Example Explanation

Explanation 1:

 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:

 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

 Leaders in an array:
 Problem Description

Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.

NOTE: The rightmost element is always a leader.


Problem Constraints

1 <= N <= 105
1 <= A[i] <= 108


Input Format

There is a single input argument which a integer array A


Output Format

Return an integer array denoting all the leader elements of the array.


Example Input

Input 1:
 A = [16, 17, 4, 3, 5, 2]
Input 2:
 A = [5, 4]


Example Output

Output 1:
[17, 2, 5]
Output 2:
[5, 4]


Example Explanation

Explanation 1:
 Element 17 is strictly greater than all the elements on the right side to it.
 Element 2 is strictly greater than all the elements on the right side to it.
 Element 5 is strictly greater than all the elements on the right side to it.
 So we will return these three elements i.e [17, 2, 5], we can also return [2, 5, 17] or [5, 2, 17] or any other ordering.
Explanation 2:
 Element 5 is strictly greater than all the elements on the right side to it.
 Element 4 is strictly greater than all the elements on the right side to it.
 So we will return these two elements i.e [5, 4], we can also any other ordering.



 Rotation Game:
Problem Description

Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.


Problem Constraints

1 <= N <= 106
1 <= A[i] <=108
1 <= B <= 109


Input Format

There are 2 lines in the input

Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.

Line 2: A single integer B.


Output Format

Print array A after rotating it B times towards the right.


Example Input

Input 1 :
4 1 2 3 4
2


Example Output

Output 1 :
3 4 1 2


Example Explanation

Example 1 :

N = 4, A = [1, 2, 3, 4] and B = 2.

Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]

Final array = [3, 4, 1, 2]

Multiplication of previous and next:

Given an array of integers A, update every element with multiplication of previous and next elements with following exceptions. a) First element is replaced by multiplication of first and second. b) Last element is replaced by multiplication of last and second last.


Input Format

The only argument given is the integer array A.
Output Format

Return the updated array.
Constraints

1 <= length of the array <= 100000
-10^4 <= A[i] <= 10^4 
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [2, 3, 8, 15, 20]

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    [85, 500, 187, 1100]



Primal Power:
Problem Description

"Primal Power" of an array is defined as the count of prime numbers present in it.

Given an array of integers A of length N, you have to calculate its Primal Power.



Problem Constraints

1 <= N <= 103

-106 <= A[i] <= 106



Input Format

First and only argument is an integer array A.



Output Format

Return the Primal Power of array A.



Example Input

Input 1:

 A = [-6, 10, 12]
Input 2:

 A = [-11, 7, 8, 9, 10, 11]

 MAx-Min:

 Given an array of integers A and an integer B, find and return the difference of B'th max element and B'th min element of the array A.


Input Format

The first argument given is the integer array A.
The second argument given is integer B.
Output Format

Return the value of B'th max element of A - B'th min element of A.
Constraints

1 <= B <= length of the array <= 100000
-10^9 <= A[i] <= 10^9 
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    2   (4 - 2 = 2)

Input 2:
    A = [5, 17, 100, 11]
    B = 1
Output 2:
    95  (100 - 5 = 95)

