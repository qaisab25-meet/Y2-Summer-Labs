from flask import Flask, render_template, request, redirect, url_for, session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = "PASSWORD"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_session['username'] = request.form['username']
        login_session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in login_session:
        return render_template('home.html', username=login_session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/fortune')
def fortune():
    if 'username' in login_session:
        birth_month = login_session['birth_month']
        fortunes = [
            "Your creativity will lead you to unexpected successes.",
            "Embrace change, for it will bring you great opportunities.",
            "Trust your instincts; they will guide you to remarkable achievements.",
            "The journey of a thousand miles begins with a single step.",
            "Kindness is the key to unlocking doors of happiness.",
            "Forgive others not because they deserve forgiveness, but because you deserve peace.",
            "If you want to buy without looking at the price, you need to work without looking at the clock.",
            "The best way to predict your future is to create it.",
            "Amir is the GOAT of CS.",
            "Abdala is going to chase you h!"
        ]
        num_letters = len(birth_month)
        final_fortune = fortunes[num_letters - 1] if num_letters <= len(fortunes) else fortunes[9]
        login_session['fortune'] = final_fortune
        return render_template('fortune.html', fortune=final_fortune)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)



