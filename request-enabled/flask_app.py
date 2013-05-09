#/usr/bin/env python
from flask import Flask,request
from processing import postme,postreadability
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    form = """
	<span>Naive Implementation</span>
        <form action="/postme" method="post">
		<input type="TEXT"" name="text" value="" />
		<input type="submit" class="submit" value="Ok" name="" />
	</form>
    <br />
	<hr />
    <br />
	<span>Using Readability</span>
    <form action="/postmeadvanced" method="post">
    	<input type="TEXT"" name="text" value="" />
		<input type="submit" class="submit" value="Ok" name="" />
	</form>

    """
    return form

@app.route('/postme',methods=["POST","GET"])
def callpostme():
	text = request.form['text']
	postme(text)

@app.route('/postmeadvanced',methods=["POST","GET"])
def callpostreadability():
	text = request.form['text']
	postreadability(text)

if __name__ == '__main__':

	port = int(os.environ.get("PORT", 5000))
	app.debug = True
	app.run(host='127.0.0.1', port=port)
