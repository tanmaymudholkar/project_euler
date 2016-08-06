#!/usr/bin/env python

def num2words(n):
    if(isinstance(n,int)):
        if(n==1):
            return "one"
        elif(n==2):
            return "two"
        elif(n==3):
            return "three"
        elif(n==4):
            return "four"
        elif(n==5):
            return "five"
        elif(n==6):
            return "six"
        elif(n==7):
            return "seven"
        elif(n==8):
            return "eight"
        elif(n==9):
            return "nine"
        elif(n==10):
            return "ten"
        elif(n==11):
            return "eleven"
        elif(n==12):
            return "twelve"
        elif(n==13):
            return "thirteen"
        elif(n==14):
            return "fourteen"
        elif(n==15):
            return "fifteen"
        elif(n==16):
            return "sixteen"
        elif(n==17):
            return "seventeen"
        elif(n==18):
            return "eighteen"
        elif(n==19):
            return "nineteen"
        elif(n==20):
            return "twenty"
        elif(n>20 and n<30):
            return "twenty"+num2words(n%10)
        elif(n==30):
            return "thirty"
        elif(n>30 and n<40):
            return "thirty"+num2words(n%10)
        elif(n==40):
            return "forty"
        elif(n>40 and n<50):
            return "forty"+num2words(n%10)
        elif(n==50):
            return "fifty"
        elif(n>50 and n<60):
            return "fifty"+num2words(n%10)
        elif(n==60):
            return "sixty"
        elif(n>60 and n<70):
            return "sixty"+num2words(n%10)
        elif(n==70):
            return "seventy"
        elif(n>70 and n<80):
            return "seventy"+num2words(n%10)
        elif(n==80):
            return "eighty"
        elif(n>80 and n<90):
            return "eighty"+num2words(n%10)
        elif(n==90):
            return "ninety"
        elif(n>90 and n<100):
            return "ninety"+num2words(n%10)
        elif(n==100):
            return "onehundred"
        elif(n>100 and n<1000):
            if(n%100!=0):
                return (num2words(n/100)+"hundredand"+num2words(n%100))
            else:
                return (num2words(n/100)+"hundred")
        elif(n==1000):
            return "onethousand"

def number_of_letters(n):
    print num2words(n)
    s=list(num2words(n).strip())
    return len(s)

no_reqd=0
for i in range(1,1001):
    print i
    no_reqd=no_reqd+number_of_letters(i)

print no_reqd
