from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = 'agy5eh;hruvgahwgo'


@app.route('/')
def cookies():
    if "c" in session: 
        print(session['c'])
    else:
        session['c'] = 0
    session['c'] = session['c'] + 1

    return render_template('index.html')

@app.route('/reroute')
def destroy():
    session.clear()

    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)
