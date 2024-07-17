from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')




@app.route('/fortune')
def fortune():
    fortunes = [
       "Your creativity will lead you to unexpected successes.",
"Embrace change, for it will bring you great opportunities.",
"Trust your instincts; they will guide you to remarkable achievements.",
"The journey of a thousand miles begins with a single step.",
"Kindness is the key to unlocking doors of happiness.",
"Forgive others not because they deserve forgiveness, but because you deserve peace.",
"if you to buy without looking at the price, you need to work without looking at the clock",
"The best way to predict your future is to create it.",
"amir is the goat of CS",
"abdala is going to chase you" 
]
    random_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=random_fortune)
if __name__ == '__main__':
    app.run(debug=True)