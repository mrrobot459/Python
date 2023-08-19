import random 

number = random.randint(1,9)

chance = 4
attempt  = 1
print("\nWellcome to my guessing Game.")
while attempt < chance:

    print("\n\nyou have only 3 attempts ")
    print (f"\nyour attempts : {attempt}")
    guess = int(input("\nCan you guess which numer I am thinking : "))
    attempt += 1
    print()
    if guess > number:
        print(f"{guess} is graeater then the number  that I choose ! ")


    elif guess < number:
        print(f"{guess} is smaller then the number that  I choose ! ")
    else:
        print(f"🅲 🅾 🅽 🅶 🆁 🅰 🆃 🆂 ! {guess} 🅸 🆂   🆃 🅷 🅴    🅽 🆄 🅼 🅱 🅴 🆁   🆃 🅷 🅰 🆃  🅸   🆃 🅷 🅸 🅽 🅺 ")
        break

if attempt >= chance :
    print(f"\nyou loose ! That number was {number}")
    

