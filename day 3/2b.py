n=int(input('enter the value of n:(odd only)\t'))
s=n
p=3
for i in range(n):
    if i>int(n/2):
        for k in range(int(i+1),n):
               print(' ',end='')
        for j in range(int(p)):
               print('*',end='')
        print('\n')
        p=p+2
    else:
     for k in range(i):
          print(' ',end='')
     for j in range(s):
          print('*',end='')
     print('\n')
     s=s-2
