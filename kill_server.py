#!/data/data/com.termux/files/usr/bin/python3
from flask import Flask
import threading
import time

app = Flask(__name__)
KILL = False

@app.route('/status')
def status():
    return "KILL" if KILL else "OK"

@app.route('/activate')
def activate():
    global KILL
    KILL = True
    return "Kill switch activated. All payloads will now self-destruct."

def run_server():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    print("[*] Kill Switch Server running on port 5000")
    print("[*] URL: http://localhost:5000/status")
    print("[*] To activate kill switch: http://localhost:5000/activate")
    run_server()
