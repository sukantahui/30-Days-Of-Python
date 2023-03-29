#check buzz number
def is_buzz_number(num):
    if num%10==7 and num%7==0:
        return True

num=int(input("Enter a number"))
if is_buzz_number(num):
    print (num,"is a buzz number")
else:
    print(num,"is not buzz number")