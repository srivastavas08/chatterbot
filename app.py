from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "ChatterBox",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter'
    ],
    # database_uri= 'mongodb+srv://cluster-flaskbank.f042j.gcp.mongodb.net/FlaskBank?retryWrites=true&w=majority')
    database_uri = 'mongodb://localhost:27017/chatterbot-database')

# data = open('C:\\Users\\AMINDE64\\chat\\chatterbot-corpus-1.1.2\\chatterbot_corpus\\data\\english' + files, "r").readlines()
# bot.train(data)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("/home/pradeep/.local/lib/python3.6/site-packages/chatterbot_corpus/data/english")

print("Try something to Begin")
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
