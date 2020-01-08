from flask import Flask, render_template, json, request

import chats

app = Flask('app')


@app.route('/')
def index_page():
  return render_template('index.html')


@app.route('/health')
def health_check():
  return "OK"


@app.route('/chat/read')
def return_chat():
  return chats.get_chat()


@app.route('/chat/send', methods=['POST'])
def receive_message():
  data = request.data
  msg = json.loads(data)
  chats.add_message(msg['message'])
  return chats.get_chat()
  

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)