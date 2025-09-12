from random import randint
guesses = 0
secret_number = randint(1, 10)
while True:
    try:
        guess = int(input("Gissa på ett heltal mellan 1 och 10: "))
        guesses += 1
    except ValueError:
        print("Ogiltig inmatning. Vänligen ange ett heltal.")
        continue

    if guess > secret_number:
        print("Du gissade för högt!")
    elif guess < secret_number:
        print("Du gissade för lågt.")
    else:
        print(f"Grattis du gissade rätt med {guesses} gissningar!")
        break
