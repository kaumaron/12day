from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np

app = Flask(__name__)

app.vars = {}

def datatime(x):
    return np.array(x, dtype=np.datetime64)

@app.route('/',methods={'GET','POST'})
def main():
    if request.method == 'GET':
        return redirect('/index')
    else:
        app.vars['stock'] = request.form['stock']
        app.vars['features'] = request.form['features']

        return redirect('/graph')

@app.route('/index', methods={'GET','POST'})
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        app.vars['stock'] = request.form['stock']
        app.vars['features'] = request.form['features']

        return redirect('/graph')

@app.route('/graph', methods={'GET','POST'})
def graph():	
    if request.method == 'POST':
        return 'Error! POST method used.'
    else:
	api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % app.vars['stock']
	session = requests.Session()
	session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
	raw_data = session.get(api_url)
	
	#plot = figure(line(datetime(raw_data['Date']),raw_data['Adj. Close'], color='#4169e1'),
	#	title='Data from Quandle WIKI set',
	#	x_axis_label='date',
	#	x_axis_type='datetime')


	#script,div = components(plot)
        return render_template('graph2.html')#, script='script', div='div')

if __name__ == '__main__':
    app.run(port=33507)
#   app.run(host='0.0.0.0',debug=True)
