from flask import *
from data import teams
from random import randint
data = teams

app = Flask(__name__)

def difference (n1, n2):
    while n1 == n2:
        n2=randint(1,14)
    return n2

@app.route('/',methods = ['GET', 'POST'])
def home():
    return redirect(url_for('main'))

@app.route('/main',methods = ['GET', 'POST'])
def main():
    team1=''
    team2=''
    
    
    
    if request.method == 'POST':
        
        action = request.form.get('choice-buttons') #Returns the string from action buttons
        action=action.split(",") #Returns list "[left/right,n1,n2]"
        if action[0]=='left':
            #Error in line 27 because it does not have access to the value in n1 and n2 because its trapped in if statement
            #Insetad I should grab from the html file using jinja or buttons to return the value
            if data[int(action[1])]['number'] > data[int(action[2])]['number']:
                
                return "That is correcto mundo"
            else:
                return "You is wrong homes"
        elif action[0]=='right':
            if data[int(action[1])]['number'] < data[int(action[2])]['number']:
                return "You is correcto Mundo"
            else:
                return "You is wrong homes"
        #Fix so that the render template is locked behind an if or something so that it doesnt reassign the numbers
        #Use an if get method for this, get method isnt shown unless you use a redirect so just fix that and numbers should stay the same
    
    if request.method == 'GET':
        c=0
        team1=''
        team2=''
        n1 = randint(1,14)
        n2=randint(1,14)
        n2 = difference(n1,n2)
        print(n1)
        print(n2)
        return render_template('main.html',teams=data, count=c, t1='', t2='', list=[n1,n2])




#NEeds at end so it keeps running
if __name__ == '__main__':
    app.run(debug=True)

