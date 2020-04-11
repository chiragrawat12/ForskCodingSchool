""" Clean the Messy salary into integers for Data Processing
salary = '$876,001' """
#submitted by: Chirag Singh from Noida
#University roll no.:- 1813313036

msySlry=input("Enter Your Salary: ")
clnSlry=msySlry.replace('$','')
clnSlry=clnSlry.replace(',','')
clnSlry=int(clnSlry)
print("Messy Salary:",msySlry,"is now cleaned:",clnSlry) 

    
