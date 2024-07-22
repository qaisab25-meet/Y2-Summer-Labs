from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase 

app = Flask(__name__,template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "PASSWORD"

firebaseConfig = {
  "apiKey": "AIzaSyAuiCUqi8OEZ0h0lOjCeBAD597YZVMGpi4",
  "authDomain": "auth-lab-6aaa6.firebaseapp.com",
  "projectId": "auth-lab-6aaa6",
  "storageBucket": "auth-lab-6aaa6.appspot.com",
  "messagingSenderId": "578072916638",
  "appId": "1:578072916638:web:2fa2fa98a3713f07df418f",
  "measurementId": "G-CKF3EQWGK1",
  "databaseURL" : "https://auth-lab-6aaa6-default-rtdb.europe-west1.firebasedatabase.app/"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']

        login_session['email'] = email
        login_session['password'] = password
        login_session['full_name'] = full_name
        login_session['username'] = username

        try:
            session['user'] = auth.create_user_with_email_and_password(email, password)
            user_id = session['user']['localId']
            user = {
                'email': email,
                'full_name': full_name,
                'username': username
            }
            db.child('Users').child(user_id).set(user)
            session['quotes'] = []
            return redirect(url_for('home'))
        except Exception:
            error = "Failed to create user. Please try again."
            return render_template('error.html', error=error)

@app.route("/signout", methods=["GET", "POST"])
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except Exception:
            error = "fail"
            return render_template('error.html', error=error)

@app.route("/home", methods=["GET", "POST"])
def home():
    if login_session.get('user'):
        if request.method == "GET":
            return render_template('home.html')
        else:
            quote = request.form['quote']
            speaker = request.form['speaker']
            quote_dict = {"text": quote, "said_by": speaker, 'uid': login_session['user']['localId']}
            db.child("Quotes").push(quote_dict)
            return redirect(url_for('thanks'))
    else:
        return redirect(url_for('main'))

@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    if login_session.get('user'):
        return render_template("thanks.html")
    else:
        return redirect(url_for('main'))

@app.route("/display", methods=["GET", "POST"])
def display():
    if login_session.get('user'):
        user_data = db.child("Quotes").get().val()
        return render_template("display.html", user_data=user_data)
    else:
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)