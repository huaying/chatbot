from chatterbot import ChatBot
from flask import Flask
from flask import request

chatbot = ChatBot(
    'Buggy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train('chatterbot.corpus.english')

app = Flask(__name__)

@app.route("/say")
def say():
    text = request.args.get('text', default='', type=str)
    return chatbot.get_response(text).text