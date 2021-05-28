from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
trainer = ListTrainer(bot)
corptrainer = ChatterBotCorpusTrainer(bot)

trainer.train(['What is your name?', 'My name is Annie'])
trainer.train(['Who are you?', 'I am a bot' ])
trainer.train(['Who created you?', 'Tony Stark', 'Dimuthu Wickramanayake', 'You?'])

corptrainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()