import random
from flask import Flask, render_template

#from random import randit

app = Flask(__name__)

@app.route('/')
@app.route('/home.html')
def home():
	return render_template("home.html")
@app.route('/aboutfadi.html')
def aboutfadi():
	return render_template("aboutfadi.html")


#@app.route("/myname: <name>")
#def nameFunc(name):
#	return render_template("home.html", title="home", name=name)

@app.route('/contctme.html')
def contctme():
	return render_template("contctme.html")
@app.route('/hacker.html')
def hacker():
	return render_template("hacker.html")
@app.route('/mylife.html')
def mylife():
	return render_template("mylife.html")
@app.route('/projects.html')
def projects():
	return render_template("projects.html")
@app.route('/projectstwo.html', methods=['post','get'])
def projects2():
	return render_template("projectstwo.html")


#@app.route('/<name>')
#def hello(name):
#	return render_template("hello.html", name=name)

@app.route('/listex.html')
def listex():
	listex= ["sjdd", "dsaf", "sdaf", "sdaf" , "asdf"]
	display= False 
	return render_template("listex.html", display=display, list=listex)
	


#@app.route('/')
#def hello():
#	return "Hello, world !"
#fadi = ['jsagfjadsgfjhasdgjfsjdf', 'ksjdbafjdsf' , 'ajsdfjhasbdf' , ',sajdfkjsd' , 'sdfdaf']
#@app.route('/fadai')
#def index(): 
#	return (random.choice(fadi))

if __name__ == "__main__":
	app.run(port=5000)


