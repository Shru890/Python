import random
import string
num= random.randint(100, 999)
alpha=list(string.ascii_uppercase)
l = random.choice(alpha)
l2 = random.choice(alpha)
for i in range(1):
    name=l+l2+str(num)
print(name)
