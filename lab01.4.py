s1=input("enter string:")
def calchigh(a):
    s=list(a)
    count=0
    ch=''
    for i in s:
        c=s.count(i)
        if c>count:
            ch=i#updating highest character
            count=c#updating highest count 
    return ch,count
ch1,count=calchigh(s1)
print("maximally occuring character is",ch1)
print("occurrence count ",count)