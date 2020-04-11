# Assignments - 6
"""
Name: 
    Clean the Messy salary from list        
Filename:
    salary2.py
Problem Statement:
    salaries = ['$876,001', '$543,903', '$2453,896'] 
    Clean the Messy salaries into integers for Data Processing
    Remove the $
    Remove the ,
    Convert into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We canuse the int() typecast to convert into integer
"""
#submitted by: Chirag Singh from Noida
#University roll no.:- 1813313036



""" *MUST READ*
In this firt piece of code i used method one which is done according to the 
hint given in the question
"""


salaries = ['$876,001', '$543,903', '$2453,896'] 
x=0
for msyslry in salaries:
    clsysum=""
    clnslry=msyslry[1:]
    clnslry=clnslry.split(',')
    for i in clnslry:
        clsysum+=i
    clnslry=int(clsysum)
    salaries[x]=clnslry
    x+=1
print("The salaries is now cleaned: ",salaries)



""" *MUST READ*
In this second piece of code i used the method which is used in previous salary
assignment by using replce()
"""


salaries = ['$876,001', '$543,903', '$2453,896'] 
i=0
for msyslry in salaries:
    clnslry=msyslry.replace('$','')
    clnslry=clnslry.replace(',','')
    clnslry=int(clnslry)
    salaries[i]=clnslry
    i=i+1
print("The salaries is now cleaned: ",salaries)



