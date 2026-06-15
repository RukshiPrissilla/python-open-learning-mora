def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return(a/b)
def Power(a,b):
    return a^b
def Remainder(a,b):
    return a%b


def select_op(choice):
    if choice=="#":
        return -1
    if choice=="$":
        return 0
    if choice not in ("+","-","*","/","^","%"):
        print("Unrecognised operation")
        return 0
    while True:
         a=input("Enter first number: ")
         if a=="#":
              return -1
         if a=="$":
              return 0
         try:
              a=float(a)
              break
         except ValueError:
              print("Not a valid number, please enter a number.")
    while True:
            b=input("Enter second number: ")
            if b=="#":
                return -1
            if b=="$":
                return 0
            
                
            try:
                b=float(b)
                break
            except ValueError:
                print("Not a valid number, please enter a number.")
        
    if choice == '+':
        print(a,"+",b,"=", Add(a,b))
    elif choice == '-':
         print(a,"-",b,"=", Subtract(a,b))
    elif choice == '*':
        print(a,"*",b,"=", Multiply(a,b))
    elif choice == '/':
        if b==0:
            print(" float division by zero ")
            print(a,"/",0,"= 0")
        else:
            print(a,"/",b,"=", Divide(a,b))
    elif choice == '^':
            print(a,"^",b,"=", Power(a,b))
    elif choice == '%':
            print(a,"%",b,"=", Remainder(a,b))
    else:
            print("Something went wrong")

    

while True:
    print("Select operation.")
    print("1.Add      :+")
    print("2.Subtract :-")
    print("3.Multiply :*")
    print("4.Divide   :/")
    print("5.Power    :^")
    print("6.Remainder:%")
    print("7.Terminate:#")
    print("8.Reset    :$")
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice)==-1):
         print("Done terminating")
         exit()
    
    
         





