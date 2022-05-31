from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
   return redirect('/login')

@app.route('/login', methods=['GET', 'POST']) 
def login():
   return render_template('index.html')

@app.route('/loggedin')
def logged():
   return render_template('loggedin.html')


if __name__ == '__main__':
   app.run(debug=True)