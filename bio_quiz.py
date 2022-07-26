
name = input('please enter your name:')
print(f"Hi {name.title()}! Let's play a simple quiz.")
prompt ='Are you ready?'
print(prompt)
answer = input("Enter yes or no: ")
if answer == "no":
    exit()
elif answer == "yes":
    def check_guess(guess, answer):
        global score
        still_guessing = True
        attempt = 0
        while still_guessing and attempt < 3:
            if guess.lower() == answer.lower(): 
                print("Correct Answer")
                score = score + 1
                still_guessing = False
            else:
                if attempt < 2:
                    guess = input("Sorry Wrong Answer, try again")
                attempt = attempt + 1
        if attempt == 3:
            print("The Correct answer is ",answer )

score = 0
print("Name the body part")
guess1 = input("Which organ pumps blood to the whole body? ")
check_guess(guess1, "heart")
guess2 = input("What is the tissue that connects muscle to the bone? ")
check_guess(guess2, "tendon")
guess3 = input("Name the largest organ of the human body.")
check_guess(guess3, "skin")
print("Your Score is "+ str(score))

 
    
