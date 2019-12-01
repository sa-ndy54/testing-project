x=int(input("enter first number\n\t\t\t"));
y=int(input("enter second number\n\t\t\t"));
z=int(input("enter third number\n\t\t\t"));
if(x>y and x>z):
    print("\t\t\t x is largest");
    elif(x==y and y==z):
        print("\t\t\t All numbers are same");
        elif(y>z and y>x):
            print("\t\t\t y is largest");
            elif(z>x and z>y):
                print("\t\t\t z is largest");
else:
    print(wrong choice);
    print(Good Bye);
    exit();
    
