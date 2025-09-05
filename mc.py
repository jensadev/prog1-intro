import random
print("Välkommen till Minecraft!")
name = input("Vad heter du? ")
print(f"Hej {name}, låt oss börja spela Minecraft!")
print("Du möter en zombie, skit också!")
player_health = 100 # spelarens hälsa, en integer
zombie_health = 50
mace = 100
while player_health > 0 and zombie_health > 0:
    player_attack = random.randint(1, 10) + mace
    print(f"Du slår zombien och gör {player_attack} skada!")
    zombie_attack = random.randint(1, 5) + 1
    player_health -= zombie_attack
    zombie_health -= player_attack
    print(f"Zombien vevar till dig för {zombie_attack} skada, du har {player_health} liv kvar!")

print(f"Du, {name}, betraktar zombiens rester, segern är din!")
