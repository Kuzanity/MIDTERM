from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/registration')
def regis():
    return render_template('registration.html')
if __name__=="__main__":
    
    app.run(host="0.0.0.0",port=5000)