values=[2,4,6,8]
print(values[0])  #2
for value in values:
    print(value,end=" ")  #2 4 6 8
print()
a=values[0:2]
for value in a:
    print(value,end=" ") # 2 4


print()
#append,update,delete,remove
numbers=[3,2,6,7,8]
numbers.append(4)  #[3,2,6,7,8,4]
print(numbers)
numbers[1]=5
print(numbers)  #[3,5,6,7,8,4]
numbers.remove(3)
print (numbers)  #[5,6,7,8,4]
del numbers[1]
print(numbers)  #[5,7,8,4]
print(numbers[2:])  #[8,4]