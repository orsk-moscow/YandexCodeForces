# single line with integers
arr = list(map(int, (str(input()).split())))
## 2 params
n = arr[0]
k = arr[1]

# single line with strings
arr = list(str(input()).split())
n = int(arr[0])
m = int(arr[1])

# pure string
arr = input()

# number if strings
n = int(input()) 
# and after that strings
arr = list(map(int, (str(input()).split(" "))))

# number if strings
f=open('input.txt','r')
n=int(f.readline())
# and after that strings
input_=[]
while n:
    n-=1
    s=f.readline()
    input_.append(s.split())
input_
