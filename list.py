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

#multidimensional list
data=[[1,1,1],[2,2,2],[3,3,3]]
print(data[1][1])  #2
data[1][1]=25
print(data)  #[[1,1,1],[2,25,2],[3,3,3]]
data[1].append(3)
print(data)  #[[1,1,1],[2,25,2,3],[3,3,3]]

#length
print(len([1,2,3]))  #3

#concatenation
a=[1,2,3]
b=[4,5,6]
print(a+b) #[1,2,3,4,5,6]

#repetition
print(["hi"]*2)  #['hi','hi']

#membership&iteration
print(3in[1,2,3]) #True
for x in [1,2,3]:
    print(x,end=" ") #1 2 3

#indexing&slicing
K=['s','d','g']
#K[2]=g
#K[-2]=d
#K[1:]=d,g