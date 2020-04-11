import random

u,c=0,0

print("----------Welcome to the Stone Paper Scisor game----------")
print()
print("###########------Game has started------########### ")

while True:
    
    ans=input("Enter:\n> Stone\n> Paper\n> Scisor\n??\n\n--> ")
    ans=ans.lower()
    if ans in ["stone","paper","scisor"]:
        comp=random.choice(["stone","paper","scisor"])
        print("\n\n\nYou:-- ",ans,"\n")
        print("  Vs")
        print("\nComputer:-- ",comp)
        if comp!=ans:
            
            if (comp=="scisor" and ans == "stone") or (comp=="stone" and ans == "scisor"):
                
                if comp=="stone":
                    print("\n\n<==========Computer Got point==========>")
                    c+=1
                
                else:
                    print("\n\n<==========You got Point==========>")
                    u+=1
            
            elif (comp=="stone" and ans == "paper") or(comp=="paper" and ans == "stone"):
                
                if comp =="paper":
                    print("\n\n<==========Computer Got point==========>")
                    c+=1
                
                else:
                    print("\n\n<==========You Got Point==========>")
                    u+=1
            
            elif (comp=="scisor" and ans == "paper") or (comp=="paper" and ans == "scisor"):
                
                if comp=="scisor":
                    print("\n\n<==========Computer Got Point==========>")
                    c+=1
                
                else:
                    print("\n\n<==========You Got Point==========>")
                    u+=1
            
            else:
                continue
        
        else:
            print("\n\n<==========Draw,Nobody will get Point==========>")
            
            
    
    else:
        print("**WARNING** Invalid input!!input again")
        
    if input("\nWant to play again??(y/n)") in "Nn":
        break
if u>c:
    print("\n\n<==========You Win==========>\n\nYour Points: {}\nCoputer Points{}: ".format(u,c))
elif c>u:
    print("\n\n<==========Computer Win==========>\n\nYour Points: {}\nCoputer Points{}: ".format(u,c))
else:
    print("\n\n<==========Draw,Nobody Win==========>\n\nYour Points: {}\nCoputer Points{}: ".format(u,c))