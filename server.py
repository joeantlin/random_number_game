from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    print('*'*80)
    print('I am Home')
    import random
    if 'count' in session:
        print(f"count session:{session['count']}")
        session['count'] += 1
    else:
        print("key 'keyname' does NOT exist")
        session['rand'] = random.randint(1, 100)
        session['count'] = 1 
        session['tries'] = 0
    return render_template('index.html')

@app.route('/theguess', methods=['POST'])
def game():
    print('*'*80)
    print('Your Guess')
    rand = session['rand']
    session['userguess'] = request.form['guess']
    if int(session['userguess']) == rand:
        print("you got it")
        session['tries'] += 1
        session['color'] = 'lightgreen'
        session['message'] = f'{rand} was the number'
    elif int(session['userguess']) < rand:
        print("too low")
        session['tries'] += 1
        session['color'] = 'red'
        session['message'] = 'Too Low'
    elif int(session['userguess']) > rand:
        print("too high")
        session['tries'] += 1
        session['color'] = 'red'
        session['message'] = 'Too High'
    if int(session['tries']) >= 5 and int(session['userguess']) != rand:
        print("You Lose")
        session['color'] = 'yellow'
        session['message'] = f'You Lose'
    print(f"random: {rand}")
    print(f"{session['tries']} tries")
    return redirect('/')
# random.randint(1, 100)

@app.route('/destroy')
def destory():
    session.clear() # clears all keyss
    #session.pop('count') # clears a specific key
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)