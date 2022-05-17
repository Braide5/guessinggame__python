while True:
    import random
    question = True
    while question:
        num = input("type the higest number you want: ")
        if num.isdigit():
            print("I like that, Let's play!")
            num = int(num)
            question = False
        else:
            print("Invalid input! Try again.")
    random_number = random.randint(1,num)
    guess = 0
    trial = 0
    while trial < 3:
        guess = input('guess a number between 1 and ' + str(num) + ":")
        if guess.isdigit():
            guess = int(guess)
        trial += 1
        if guess < random_number:
                print("sorry, try again too low.")
        elif guess > random_number:
            print("sorry, try again. too high.")
        elif guess == random_number:
             print("you got it!")

    print("you failed")





