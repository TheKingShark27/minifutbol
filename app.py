from flask import *


app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    return redirect(url_for('main'))

@app.route('/main',methods = ['GET', 'POST'])
def main():
    return render_template('main.html')




#NEeds at end so it keeps running
if __name__ == '__main__':
    app.run(debug=True)

