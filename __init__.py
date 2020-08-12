from mycroft import MycroftSkill, intent_file_handler


class CoinFlip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('flip.coin.intent')
    def handle_flip_coin(self, message):
        side = ''

        self.speak_dialog('flip.coin', data={
            'side': side
        })


def create_skill():
    return CoinFlip()

