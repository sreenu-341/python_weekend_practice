# 1. write a program fro printing number in the range excluding that are multiples of 3 and 5 ?
num=int(input('enter an upper range number :'))
print('range excluding multiples of 3 and 5 are : ')
for i in range(0,num):
    if i%3!=0 and i%5!=0:
        print(i,end=' ')