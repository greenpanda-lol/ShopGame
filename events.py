import random
import game
# összes esemény
events = {
 "rablas": {
    "id": "r",
     "moneyeffect": -500


 },

 "kisrablas":{
     "id": "kr",
     "moneyeffect": -500

 }
}
def eventchoice():
    event = random.choice(list(events.items()))
    return event
# választ egy eventet

def effect():
    game.dollar += event["moneyeffect"]
    print (f' A pénzed: {game.dollar}')
# végrehajtja az event hatását
# nem műkszik :(




