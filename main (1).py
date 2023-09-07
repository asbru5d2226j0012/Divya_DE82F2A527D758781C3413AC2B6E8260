#1.1 implement a recursive function to calculate the factorial of a given number
def fact_ rec(n) 
if n==0 or n ==1
    return 1
else:
     return n*fact_rec(n-)
number=2
res=fact rec(number)
print ("The factorial of {}is {}").format (number,res))