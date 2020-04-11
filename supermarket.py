# Day 5

# Assignments - 9

"""
Name: 
    Supermarket      
Filename:
    supermarket.py 
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Sample Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
""" 





sdict=dict()
print("Enter Items: ")
while True:
    str1=input("> ")
    if str1:
        lst=str1.split()
        val=int(lst[-1])
        lst.remove((lst[-1]))
        key=" ".join(lst)
        if key in sdict:
            sdict[key]+=val
        else:
            sdict[key]=val
    else:
        break
print("\n\n")
[print(key,val) for key,val in sdict.items()]    
    
    
