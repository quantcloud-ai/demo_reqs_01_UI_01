from flask import Flask
import json

app = Flask(__name__)

f = open('instruments.json', 'r')
instruments = json.load(f)
f.close()

f = open('options_dict.json','r')
options = json.load(f)
f.close()

@app.route('/options/<instrument>')
def get_options(instrument):
    return {'options': options[instrument]}


@app.route('/')
def get_instruments():
    return {'instruments': instruments}


if __name__ == '__main__':
    app.run()
