number = int(input("Skriv in ett heltal som du vill gångra: "))
for i in range(2, 11):
    print(f"{number} * {i} är { number * i }")

def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Felaktig inmatning")

number = input_int("Skriv ett tal du vill gångra: ")
for i in range(1, 11):
    print(f"{number} * {i} är { number * i}")
