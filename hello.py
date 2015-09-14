#/usr/bin/env python

from flask import Flask, request, redirect, make_response, abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
	return "<h1>Hello, Flask!</h1>"

@app.route('/response')
def testResponse():
	res = make_response('<h1>Hello, this is a response object</h1>')
	res.set_cookie('test', 'opps')
	return res

'''@app.route('/abort/<id>')
def testAbort(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>No error. %s' % user.name'''

@app.route('/redirect')
def testRedirect():
	return redirect('http://localhost:5000/browser')

@app.route('/user/<name>')
def user(name):
	return "<h1>Hello, %s!</h1>\
	<a href='/'>Home</a>" % name

@app.route('/browser')
def browser():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
	manager.run()
