from mycroft import MycroftSkill, intent_file_handler
import random

class CoinFlip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('flip.coin.intent')
    def handle_flip_coin(self, message):
        try:
            coin = ["head", "number"]
            side = random.choice(coin)
            #result = {'side': message.data.get("side")}
            self.speak_dialog('flip.coin', data={'side': side})
	    #self.speak_dialog("response", data=result)
            pass
        except:
            #self.speak_dialog("error")

def create_skill():
    return CoinFlip()

