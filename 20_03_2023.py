f_w=open('rifat.txt','w');
f_w.write("I am adding my all message");
print(f_w);

##Print
x=2;
print('x',x);
print('x' ,'y', sep='');
print("x" ,"y",sep=":");
print('x','y',sep=')=');

for i in 'Python':
    print(i);

for i in 'Bangladesh':
    print(i);

for i in ('Abu Al Shahriar Rifat'):
    print(i);

f1w1=open('print_function.txt','w');
print("Print function",file=f1w1);
f1w1.close();

myName=input("Enter Name=");
print("My name is "+ myName);

age=int(input("Enter age ="));
print("My age is ", age);
print(type (age));

##using help()
str1='Python';
print(str1.upper())
print(str1.isalpha())

##range function
for x in range(1,10,2):
    print(x);

for x in range(10,1,-1):
    print(x);

list1=list(range(1,20));
print(list1);

##string






