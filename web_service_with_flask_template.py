from flask import render_template
from flask import request
from flask import Flask
import pandas as pd
import json

app = Flask(__name__)

columns = ['ticker','longName','sector','industry','price','market_cap','previous_close','volume','avg_volume','open','options_ttl_interest','options_ttl_volume']

f = open('instruments.json', 'r')
instruments = json.load(f)
instruments = pd.DataFrame(instruments)[columns].fillna('').to_dict('records')
f.close()

f = open('options_dict.json','r')
options = json.load(f)
f.close()

@app.route('/options/<instrument>')
def get_options(instrument):
    return {'options': options[instrument]}


@app.route('/instruments')
def get_instruments():
    return {
        'data': instruments,
        'recordsFiltered': len(instruments),
        'recordsTotal': len(instruments),
        'draw': request.args.get('draw', type=int),
    }


@app.route('/')
def index():
    return render_template('simple_table.html', title='Demo', table_columns=columns)



if __name__ == '__main__':
    app.run()
