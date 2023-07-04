def even(list):
    l1=[]
    for i in list:
        if i%2 == 0:
            l1.append(i)
    return l1




l=[1,2,3,4,5,6,7,8,9]
l2=even(l)
print(l2)
