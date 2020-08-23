# write a program that checks the specified number is armstrong number ?


a=int(input('enter a number: \t'))
sum=0
b=a
while a>0:
    rem=a%10
    sum=sum+(rem**3)
    a=int(a/10)
if sum==b:
    print(b,'\t is Armstrong numbber')
else:
    print(b,'\t is not an Armstrong number')

# print(order(a))