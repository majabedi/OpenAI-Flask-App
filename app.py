from chatbot import ChatBot
from flask import Flask, jsonify, request

app = Flask(__name__)

api_key = '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'
bot = ChatBot(api_key, "you are a helpful assistant.")
bot.initialize()

@app.route('/', methods = ['POST'])
def send_request():
    new_query = request.get_json()['query']

    if new_query != '':
        answer = bot.request(new_query)
    else:
        answer = "Sorry but your query is blank."
    
    return jsonify({"Answer": answer, "Chat History Length": len(bot.chat_history)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)