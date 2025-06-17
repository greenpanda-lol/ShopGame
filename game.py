# alap változók
#mükszik
dollar = 0
day = 1
level = 1
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
    b()
    a("FEJLESZTÉSEK|  +NAP  |BEFEKTETÉS")
    a("      |     |    |   |     |    ")
    a("      f     |    n   |     b    ")

menu()