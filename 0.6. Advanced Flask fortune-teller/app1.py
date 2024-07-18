from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', month=birth_month))

@app.route('/fortune/<month>')
def fortune(month):
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
        "Abdala is going to chase you.!"
    ]
    

    num_letters = len(month)
        
    final_fortune = fortunes[9]
    if num_letters <len(fortunes):
       final_fortune=fortunes[num_letters-1]
        
    return render_template("fortune.html", fortune=final_fortune)
if __name__ == '__main__':
    app.run(debug=True)



