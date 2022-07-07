from flask import Flask , render_template

from flask import json
 



app = Flask(__name__)
app.config.from_object('config')
from .utils import get_candidats
@app.route('/')
def hello():
   return   render_template('index.html')
@app.route('/list',methods=['GET', 'POST'])
def list():
 candidats = get_candidats()
 return render_template("list.html",candidats=candidats)
@app.route('/resultat', methods=['POST'])
def resultat():
 name = request.form.get("name")
 return render_template("list.html",candidats=candidats)
if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)
