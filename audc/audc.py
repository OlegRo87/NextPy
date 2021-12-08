import json
import random


class TestWebserver:
    def __init__(self, bot_name, bot_id):
        self.bot_name = bot_name
        self.bot_id = bot_id

        self.intents = []

    def get_name(self):
        """return the name of the bot"""
        return self.bot_name

    def __str__(self):
        """print type and name of the animal: override by every subclass"""
        return "{} {} {}".format(type(self).__name__, self.bot_name, self.bot_id)


class TestBot1(TestWebserver):
    def __init__(self, bot_name, bot_id, ):
        super().__init__(bot_name, bot_id)

    def functions(self, function):
        file = open("/home/oleg/PycharmProjects2/NextPy/audc/bots.json", 'r')
        data = json.loads(file.read())
        if function in data["bots"]['bot_1'][2].__str__():
            print("playing_sound")
        else:
            print("error")

    def __str__(self):
        """print bot name"""
        return super().__str__()


class TestBot2(TestWebserver):
    def __init__(self, bot_name, bot_id):
        super().__init__(bot_name, bot_id)

    def get_welcome(self, welcome='Hi, I am a bot'):
        print(welcome)

    def __str__(self):
        """print bot name"""
        return super().__str__()


class TestBot3(TestWebserver):
    def __init__(self, bot_name, bot_id):
        super().__init__(bot_name, bot_id)

    def auth(self, username, password, token):
        if username == "oleg" and password == 12345:
            print("auth success by basic")
        elif token == "olegrohlin12345":
            print('auth success by basic by outh')
        else:
            print("please provide a correct log-in info")

    def __str__(self):
        """print bot name"""
        return super().__str__()


def main():
    bot1 = TestBot1("My name is: bot-Oleg and my ip is: ", random.randint(1, 9))
    print(bot1)
    bot1.functions("play_sound")
    bot2 = TestBot2("My name is: bot-Olga and my ip is: ", random.randint(10, 19))
    print(bot2)
    bot2.get_welcome("bot-olga")
    bot3 = TestBot3("My name is: bot-Ole and my ip is: ", random.randint(20, 29))
    print(bot3)


main()
