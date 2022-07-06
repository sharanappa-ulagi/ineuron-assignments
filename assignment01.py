# Question 01
for i in range(2000,3001):
     if(i%7==0 and (i%5!=0)):
         print(i, end=',')

# Question 02
first_name=input("enter first name: ")
last_name=input("enter last name: ")

def reversed_name(arr):
    reverse=""
    for i in arr:
        reverse=i+reverse
        
    return reverse

print(reversed_name(first_name),reversed_name(last_name))


# Question 03

r=12.0
pi = 3.1415926535897931
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

