# to concatenate two lists index-wise with zip and without zip function
# with zip function
l1=["M","na","i","Ke"]
l2=["y","me","s","lly"]
l3=[]
for i,j in zip(l1,l2):
    l3.append(i+j)
print(l3)
print(" ".join(l3))

#without zip function
l1=["M","na","i","Ke"]
l2=["y","me","s","lly"]
l3=[]
j=0
for i in range(len(l1)):
    l3.append(l1[i]+l2[j])
    j=j+1
    
print(" ".join(l3))
