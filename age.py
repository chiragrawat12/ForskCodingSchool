"""Take the age as input from the user and print whether he is a infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen"""
#submitted by: Chirag Singh from Noida
#University roll no.:- 1813313036

age=int(input("Enter Age: "))
if(age==1 or age==0):
    print("Infant")
elif(age>1 and age<18):
    print("Child")
elif(age>=18 and age<60):
    print("Adult")
else:
    print("Senior Citizen")
    

