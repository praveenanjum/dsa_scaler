def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a=input().split()
    b=int(input())

    def rev(i,j,arr):
        i=i
        j=j
        while(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i=i+1
            j=j-1
    n=int(a[0])
    b=b%n
    rev(1,n,a)
    rev(1,b,a)
    rev(b+1,n,a)
    for i in range (1,n+1):
        print(a[i],end=" ")
    return 0

if __name__ == '__main__':
    main()