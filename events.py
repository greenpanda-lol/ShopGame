import random
import game

# összes esemény

events = {
 "rablas": {
    "id": "r",
     "moneyeffect": -500,
     "text": "Az éjjel kirabolták a boltodat! 500 Dollárt vittek el."
 },

 "kisrablas": {
     "id": "kr",
     "moneyeffect": -200,
     "text": "Az éjjel kirabolták a boltodat! 200 Dollárt vittek el."
 },

 "palyazat": {
    "id": "p",
     "moneyeffect": 500,
     "text": "A boltod megnyert egy pályázatot! A pénzdíj 500 Dollár, és kaptatok egy menő oklevelet"
 },

 "adomanyok": {
    "id": "ad",
    "moneyeffect": 200,
    "text": "A boltod kisebb, nagyobb adományokból egészen sok pénzt gyűjtött össze!"
 },

 "adocsalas": {
    "id": "acs",
    "moneyeffect": -1000
    "text": "Lebuktál, hogy adócsaló vagy. Az állam megbüntetett -$1000 dollárra."

 },

}


def eventChoice():
    event = random.choice(list(events.items()))
    return event
# választ egy eventet

def eventEffect():
    game.dollar += eventChoice.event["moneyeffect"]
    print(f'{eventChoice.event["text"]}')
# végrehajtja az event hatását
# nem műkszik :(

def eventHappen():
    eventChoice()
    eventEffect()


