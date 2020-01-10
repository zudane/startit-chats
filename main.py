from flask import Flask, render_template


app = Flask('app')


@app.route('/')
def index_page():
  return render_template('index.html')

@app.rout(health')
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)