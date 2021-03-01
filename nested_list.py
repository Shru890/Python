'''
Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''
d={} 
for _ in range(int(raw_input())): 
    Name=raw_input() 
    Score=float(raw_input())
    d[Name]=Score 
v=d.values()
second=sorted(list(set(v)))[1] 
second_lowest=[] 
for key,value in d.items():  
    if value==second: 
        second_lowest.append(key) 
second_lowest.sort() 
for name in second_lowest: 
    print name 
