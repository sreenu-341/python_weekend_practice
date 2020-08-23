# write a program to calculate sum of digits in number ?


a=int(input('enter a number ;\t'))
sum=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=int(a/10)
print(sum)