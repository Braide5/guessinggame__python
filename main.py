while True:
    import random
    random_number = random.randint(1,10)
    guess = 0
    trial = 0
    while trial < 3:
        guess = int(input('guess a number between 1 and 10 :'))
        trial += 1
        if guess < random_number:
                print("sorry, try again too low.")
        elif guess > random_number:
            print("sorry, try again. too high.")
        elif guess == random_number:
             print("you got it!")
    print("you failed")





