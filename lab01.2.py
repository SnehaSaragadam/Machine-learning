def calrange(a):
    if len(a)<3:
        return "Range determination not possible"
    else:
        m=max(a)
        n=min(a)
        r=m-n#range is max-min
        s=f"{r}({m}-{n})"
        return s
a=eval(input("enter list:"))
print(calrange(a))










