from flask import Flask, render_template, jsonify

app = Flask('app')

@app.route('/')
def index_page():
  return render_template('index.html')

@app.route('/health')
def health_check():
  return "OK"

@app.route("/chats/lasi")
del ielasit_chatu():
  chata_rindas = []
  with open("chats.txt", "r") as f:
    for rina in f:
      chata_rindas.append(rinda)

return jsonify({"chats":chata_rindas})

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)