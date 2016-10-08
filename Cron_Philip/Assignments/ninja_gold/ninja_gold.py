from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = 'IgotThisDude!'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html', goldCount=session['gold'], activity=session['activities'])

@app.route('/process_money', methods=['POST'])
def process():
    locations = {
    'farm':random.randint(10, 20),
    'cave':random.randint(5, 10),
    'house':random.randint(2, 5),
    'casino':random.randint(-50, 50),
    }
    if request.form['location'] in locations:
        result = locations[request.form['location']]
        session['gold'] = session['gold'] + result
        session['activities'].append("{} {} golds from the {} ({})".format(('lost', 'Earned')[result > 0], abs(result), request.form['location'], datetime.datetime.now()))
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)