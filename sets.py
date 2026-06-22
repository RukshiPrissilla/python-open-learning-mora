#set of integers
my_set={1,4,5}
print(my_set)  #{1,4,5}

#set with multiple data types
r_set={1,("ef","hi","btt"),7.5} 
print(r_set)  #{1,("ef","hi"),4.9}

#no duplicates
t_set={1,2,1,2,3}
print(t_set)  #{1,2,3}

#make set from a list
d_set=set([1,2,5,9,8])
print(d_set)   #{1,2,5,8,9}  with out set before list it doesnt give curly brac & no change in the numbers order

#set with mutable items cause error
#set={[1,2,3],4}