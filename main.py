from flask import Flask , render_template
import models
 
from flask import json
app = Flask(__name__)

@app.route('/')
def hello():
   return   render_template('index.html')
@app.route('/list',methods=['GET', 'POST'])
def list():
 candidats = models.Candidat.query_all()
 print("Liste des Candidats")
 for Candidat in personnes:
     print(candidat)
 return render_template("list.html",candidats=json.dumps(candidats))
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
