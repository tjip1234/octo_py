import time
import random
#import simpleaudio as sa
#variables
alive = 1
playerHp = 100
enemyHp = 20
gold = 0
goldBaseDrop = 10
playerBaseDamage = 10
enemyBaseDamage = 5
enemyName = None

def main ():
        direction()
        print("You walked " + direction_string)
        encounter()

def direction():
    global direction_string
    random_direction = random.randrange(1,5)
    if random_direction == 1:
        direction_string = "to the left"
    elif random_direction == 2:
        direction_string = "to the right"
    elif random_direction == 3:
        direction_string = "straight forward"
    elif random_direction == 4:
        direction_string = "backwards"
    elif random_direction == 5:
        direction_string = "in no general direction"
    else:
        direction_string = "you fucked up the code nigga"

def fight():
    global enemyName
    global playerHp
    global enemyHp
    global gold
    global alive
    print("You've encountered a " + enemyName + "!")
    print("Do you want to fight or do you run? (-5 HP)")
    forr = input("(fight/run) ")
    if forr == "fight":
        enemyHp = 20
        while playerHp > 0 and enemyHp > 0:
            playerTotalDamage = playerBaseDamage*(random.randrange(8,13)/10)
            enemyHp -= playerTotalDamage
            if enemyHp > 0:
                print("You did " + str(playerTotalDamage) + " damage. The " + enemyName + " now has " + str(enemyHp) + " HP")
                time.sleep(2)
                enemyTotalDamage = enemyBaseDamage*(random.randrange(8,13)/10)
                playerHp -= enemyTotalDamage
                if playerHp > 0:
                    print("The " + enemyName + " did " + str(enemyTotalDamage) + " damage. You now have " + str(playerHp) + " HP")
                    time.sleep(2)
                else:
                    print("The " + enemyName + " did " + str(enemyTotalDamage) + " damage. You now have 0 HP")
                    print("You've died. Game over...")
                    alive = 0
            else:
                goldTotalDrop = int(goldBaseDrop*(random.randrange(10,21)/10))
                gold += goldTotalDrop
                print("You did " + str(playerTotalDamage) + " damage. The " + enemyName + " died and dropped " + str(goldTotalDrop) + " gold!")
                print("You've got " + str(playerHp) + " HP and " + str(gold) + " gold.")
    else:
        playerHp -=5
        if playerHp > 0:
            print("You ran away and lost 5 HP. Current HP: " + str(playerHp))
        else:
            print("You ran away and lost 5 HP.")
            print("You've died. Game over...")
            alive = 0

def town():
    global playerHp
    if playerHp<51:
        playerHp +=50
        print("You come across a town! You get healed for 50 HP. You now have " + str(playerHp) + " HP.")
    else:
        playerHp=100
        print("You come across a town! You get fully healed.")
    print("There also is a blacksmith in the town! Would you like to buy something?")
    enterBlacksmith = input("(yes/no) ")
    if enterBlacksmith=="yes":
        print("You enter the blacksmith. You can buy:")
    else:
        print("You leave the town")

def trader():
    global playerHp
    global gold
    buyAnotherPotion = "yes"
    print("You've encountered a trader! They will trade a health potion (+30HP) for 50 gold. Do you want to buy it?")
    buyPotion = input("(yes/no) ")
    while buyAnotherPotion=="yes":
        if buyPotion == "yes":
            if gold >= 50:
                gold -=50
                playerHp += 30
                if playerHp >= 70:
                    print("You have bought a potion. It has fully healed you.")
                    buyAnotherPotion = "no"
                else:
                    print("You have bought a potion. You now have " + str(playerHp) + " HP.")
                    print("Do you want to buy another potion?")
                    buyAnotherPotion = input("(yes/no) ")
            else:
                print("You don't have enough money to buy the potion. You wander on.")
                buyAnotherPotion = "no"
        else:
            print("You don't buy the potion and wander on.")
            buyAnotherPotion = "no"

def encounter():
    global enemyName
    global playerHp
    roll = random.randrange(0,10)
    if roll==0:
        town()
    elif roll==1:
        trader()
    elif roll==2:
        enemyName="1"
        fight()
    elif roll==3:
        enemyName="2"
        fight()
    elif roll==4:
        enemyName="3"
        fight()
    elif roll==5:
        enemyName="4"
        fight()
    elif roll==6:
        enemyName="5"
        fight()
    elif roll==7:
        enemyName="6"
        fight()
    elif roll==8:
        enemyName="7"
        fight()
    else:
        enemyName="8"
        fight()


while alive== 1:
    main()
    pass
