# Assignments - 7
"""
Name: 
    Shopping List        
Filename:
    shopping.py
Problem Statement:
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.
Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app
    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE
    Step 6: print out the list
"""
#submitted by: Chirag Singh from Noida
#University roll no.:- 1813313036


shopglst=[]
print("if you'r done adding items in your list then type 'DONE'")
print("Now start adding items in your list: ")
while True:
    items=input(">")
    if (items!="DONE"):
        shopglst.append(items)
    else:
        break
print("\n\nYour Items in list are : ")
for i in shopglst:
    print(">",i)  