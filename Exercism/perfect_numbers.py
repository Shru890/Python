def classify(number):
    value = 1
    li=[]
    sum=0
    if number>0:
    	for value in range(1, number):
       		if number % value == 0:
        		li.append(value)
    	for i in li:
    		sum+=i
    	if sum==number:
    		return("perfect")
    	elif sum>number:
    		return("abundant")
    	else:
    		return("deficient")
    else:
    	raise ValueError("Non Positive and Zeros are rejected")

number=int(input())
ans=clasify(number)
print(ans)
