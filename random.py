#to count the occurence of items in a list
li=list(map(int,input("Enter the is list values::").split(" ")))
n=len(li)
dic={x:li.count(x) for x in range(n)}
dic={x:y for x,y in dic.items() if y!=0}
print(dic)

#alphabet rangoli
import string
def print_rangoli(size):
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')   for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

