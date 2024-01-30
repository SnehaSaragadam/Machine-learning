def countpairs(a):
    count=0
    for i in a:
        for j in a:
            if i+j==10:#checking if sum is 10
                count+=1
    return count
a=[2,7,4,1,3,6]
print("count=",countpairs(a))


