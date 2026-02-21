import events
Game = True
# alap változók
dollar = 0
day = 1
level = 1
shopname = input("Mi legyen a boltod neve?")
# még ide írd azt ami fontos

# ez csak nekem lesz gyorsabb xd
def a(text):
    print(text)
def b():
    print()

# menü
def menu():
    a("ShopGame")
    b()
    a(f"» PÉNZ: {dollar}$")
    a(f"» NAP: {day}.")
    a(f"» SZINT: {level}.")
    a(f"» NÉV: {shopname}.")
    b()
    a("FEJLESZTÉSEK|  +NAP  |BEFEKTETÉS")
    a("      |     |    |   |     |    ")
    a("      f     |    n   |     b    ")
    menuaction = input("Mit csinálsz?")
    if menuaction == "n":
        newDay()
    else:
        print("Ilyen akció nincs!")
        menu()
# új nap kezdése
def newDay():
    global day, dollar
    print("Új nap virradt.. éjszaka:")

    dollars = events.eventHappen(dollar) # ez a fontos, így nem kell, h ott is be legyen importálva

    day += 1
    print(f'A mai nap a {day}. nap.')
    dollar += 100
    print(f'Az előző napi bevételed: 100 Dollár (100 Dollár hozzáadva a kasszához')

def game():
    menu()
# az alap játékot futtató metódus (sztem parktikusabb lesz így, meg jobban néz ki, de nyugodtan szedd ki)

while Game:
    game()
