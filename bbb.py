import random

item_list=["rock","paper","scissor"]
comp=random.choice(item_list)
retry=input("enter play (p)& break (b) the game :")


while retry=="p":
    user=input("enter item_list(paper,scissor,rock):")
    comp=random.choice(item_list)
    print(f"user choice ={user}\ncomputer_choice={comp}") 
    
    
    if comp==user:
        print("tie")
           
    elif comp=="paper":
        if user=="rock":
            print("comp win")      
        else:
            print("user win ")
    
    elif comp=="rock":
        if user=="scissor":
            print("comp win")
        else:
            print("user win")
            
    elif comp=="paper":
        if user == "scissor":
            print("user win")
        else:
            print("comp win")
            
            
    retry=input("enter play (p)& break (b) the game : ")
else:
       
    print("you want to break the game") 

