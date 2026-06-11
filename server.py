from flask import Flask
app = Flask(__name__)

KILL = False

@app.route('/status')
def status():
    return "KILL" if KILL else "OK"

@app.route('/activate')
def activate():
    global KILL
    KILL = True
    return "Kill switch activated"

app.run(host='0.0.0.0', port=443)
