import calendar 

#Calendar in python 

print("Choose month you like as [1,2,3,4,5,6,7,8,9,10,11,12] \ n")

y=int(input('year : '))
m=int(input('month : '))
print(calendar.month(y,m))
