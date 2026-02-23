import random
# kiszedtem a game importálását, mert nem kell

# összes esemény

events = {
 "rablas": {
    "id": "r",
     "moneyeffect": -500,
     "text": "Az éjjel kirabolták a boltodat! 500 Dollárt vittek el.",
     "level": 100
 },

 "kisrablas": {
     "id": "kr",
     "moneyeffect": -200,
     "text": "Az éjjel kirabolták a boltodat! 200 Dollárt vittek el.",
     "level": 100
 },

 "palyazat": {
    "id": "p",
     "moneyeffect": 500,
     "text": "A boltod megnyert egy pályázatot! A pénzdíj 500 Dollár, és kaptatok egy menő oklevelet",
     "level": 100
 },

 "adomanyok": {
    "id": "ad",
    "moneyeffect": 200,
    "text": "A boltod kisebb, nagyobb adományokból egészen sok pénzt gyűjtött össze!",
    "level": 100
 },

 "adocsalas": {
    "id": "acs",
    "moneyeffect": -1000,
    "text": "Lebuktál, hogy adócsaló vagy. Az állam megbüntetett -$1000 dollárra.",
    "level": 100
 },

 "kisadomanyok": {
    "id": "kad",
    "moneyeffect": 50,
    "text": "A boltod kisebb adományokból, sikeresen összegyűjtött +50$-t.",
    "level": 1
 }

}


def eventChoice(level):
    validEvents = [event for event in events.values() if event ["level"] == level]
    return random.choice(validEvents)
# választ egy eventet

# def eventEffect():
    game.dollar += eventChoice.event["moneyeffect"]
    print(f'{eventChoice.event["text"]}')
# végrehajtja az event hatását
# nem műkszik :( 

def eventHappen(dollar, level):
    event = eventChoice(level)
    print(event["text"])
    return dollar + event["moneyeffect"]