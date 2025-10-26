from flask import *
from data import teams
from random import randint
data = teams

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    return redirect(url_for('main'))

@app.route('/main',methods = ['GET', 'POST'])
def main():
    c=0
    team1=''
    team2=''
    num=[]
    for i in range(50):
        num.append(randint(1,14))
    action = request.form.get('main')
    if action=='left':
        if data[num[0]]['number'] > data[num[4]]['number']:
            return "That is correcto mundo"
        else:
            return "You is wrong homes"
    elif action=='right':
        if data[num[0]]['number'] < data[num[4]]['number']:
            return "You is correcto Mundo"
        else:
            return "You is wrong homes"
        
    
    return render_template('main.html',teams=data, count=c, t1=team1, t2=team2,nums=num)




#NEeds at end so it keeps running
if __name__ == '__main__':
    app.run(debug=True)

