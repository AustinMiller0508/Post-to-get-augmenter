from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def inMarket():
    if request.args['location'] == 'florida':
        return 'Listener is IM'
    else:
        return 'Listener is OOM'
