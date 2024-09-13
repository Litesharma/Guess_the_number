import random

print("Choose any a number greater then 1 and less then 100 ")
comp_num = random.randint(1,100)
count=0
print("----------------------------------------------------")
while(True):
    count+=1
    user = (input("enter a number or Quit the Game {Q} : "))
    if(user.lower()=='q'):
        print("----You Quit------")
        break
    user_num=int(user)
    if( user_num < 1 or user_num > 100):
        print("Please enter a number greater then 1 and less then 100")
    else:
        if(user_num > comp_num):
            print("Lower number please...")
        elif(user_num < comp_num):
            print("greater number please...")
        else:
            print("-------YOU WIN----------")
            print(f"you guessed it right in {count} turn ")
            break
        
print("----------GAME OVER-----------")