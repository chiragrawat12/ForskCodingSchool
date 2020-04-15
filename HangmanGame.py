''''***********************HANGMAN GAME :-********************************'''

import random

Sports=['archery','badminton','cricket','bowling','boxing','curling','tennis','skateboarding','surfing','hockey','figure skating','yoga','fencing','fitness','gymnastics','karate','volleyball','weightlifting','basketball','baseball','rugby','wrestling','high jumping','hang gliding','car racing','cycling','running','table tennis','fishing','judo','climbing','pool','shooting','horse racing','horseback riding','golf','football']
Vegetables=['tomato' ,'beetroot','brussel sprouts','peas','zucchini','radish','sweet potato','artichoke','leek','cabbage','celery','chili','garlic','basil','coriander','parsley','dill','rosemary','oregano','cinnamon','saffron','green bean','bean','chickpea','lentil','carrot','broccoli','asparagus','cauliflower','corn','cucumber','eggplant','green pepper','lettuce','mushrooms','redpepper','pumpkin','potato','onion',]
Fruits=['apple','watermelon','orange','pear','cherry','strawberry','nectarine','grape','mango','blueberry','pomegranate','carambola','plum','banana','raspberry','mandarin','jackfruit','papaya','kiwi','pineapple','lime','lemon','apricot','grapefruit','melon','coconut','avocado','peach']
StatesInIndia=['Andra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telagana','Tripura','Uttaranchal','Uttar Pradesh','West Bengal']
# Fruits=['apple','carrot'] **uncomment this for testing**


while True:
    SorQ=int(input("1.Start Game\n2.Quit Game\n(Enter 1 or 2):"))
    if SorQ == 1:
        print("Welcome to Hangman Game-You have 5 chances to guess the word\nBest of luck!")
        while True:#Loop is for when user is giving wrong inputs 
        
            cat=int(input("1.Vegetables\n2.Fruits\n3.States in India\n4.Sports\n(Enter no. 1-4): "))
            
            #if-elif-else statements to choose secret names in chosen category
            if cat == 1:
                secretWord=random.choice(Vegetables)
                break
            elif cat == 2:
                secretWord=random.choice(Fruits)
                break
            elif cat == 3:
                secretWord=random.choice(StatesInIndia)
                break
            elif cat == 4:
                secretWord=random.choice(Sports)
                break
            else:
                print("Invalid Inpu!! Enter Again")
    else:
        print("\nThankyou for being here")
        print("Quiting this Game........")
        break
    good_guess=[]
    bad_guess=[]
    Sw=[]
    for x in secretWord:
        if x not in Sw:
            Sw.append(x)
    Sw="".join(Sw)
    

    while len(bad_guess) < 5 and len(good_guess) != len(Sw):
        
        for letter in secretWord:
            if letter in good_guess:
                print(letter ,end=" ")
            else :
                print("_",end=" ")
        print("\n\n*********Strikes used :",len(bad_guess),"/5**********\n")
        
        
        guess=input("Enter Your Guess: ").lower()#taking guess from user
        
        if len(guess)!=1:
            print("\n**********Warning!! You can enter only one letter**********\n")
            continue
        elif not guess.isalpha():
            print("\n**********Warning!! Enter only letters********\n")
            continue
        elif guess in good_guess:
            print("/n********You have already entered the letter before**********/n")
            continue
        else:
            if guess in secretWord :
                good_guess.append(guess)
            
            else:
                print("\n**********Wrong Guess**********\n")
                bad_guess.append(guess)
            
        
        if len(good_guess)==len(Sw):
            print("\n-----You Won!! Finally you guessed the word {}-----".format(secretWord))
            break
        else:
            continue
            
    
    else:
        print("\n-----You loose!!You didn't guess it: My secret word was {}-----".format(secretWord))
            
    
    
    