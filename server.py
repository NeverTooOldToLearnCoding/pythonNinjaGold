from flask import Flask, render_template, request, session, redirect
import datetime
import random
app = Flask(__name__)
app.secret_key = "Thisisasecret"

@app.route('/')
def gen():
	# session.clear()
	#keep track of gold, datetime
	if 'gold' not in session:
		session['gold'] = '0'
		session['activities'] = ''
	return render_template("index.html", activities = session['activities'],gold = session['gold'])

@app.route('/process_money', methods=['POST'])
def processer():
	y = str(datetime.datetime.now())
	if request.form['building'] == 'farm':
		x = random.randrange(10,21)
		session['gold'] = str(int(session['gold']) + x)
		session['activities'] += "<p class='green'>Earned " + str(x) + " golds from the farm! (" + y + ")</p>"
		print(session)
	if request.form['building'] == 'cave':
		x = random.randrange(5,11)
		session['gold'] = str(int(session['gold']) + x)
		session['activities'] += "<p class='green'>Earned " + str(x) + " golds from the cave! (" + y + ")</p>"
		print(session)
	if request.form['building'] == 'house':
		x = random.randrange(2,6)
		session['gold'] = str(int(session['gold']) + x)
		session['activities'] += "<p class='green'>Earned " + str(x) + " golds from the house! (" + y + ")</p>"
		print(session)
	if request.form['building'] == 'casino':
		z = random.randrange(0,2)
		if z == 0:
			x = random.randrange(0,51)
			session['gold'] = str(int(session['gold']) - x)
			session['activities'] += "<p class='red'>Entered a casino and lost " + str(x) + " golds... Ouch.. (" + y + ")</p>"
		print(session)
		if z == 1:
			x = random.randrange(0,51)
			session['gold'] = str(int(session['gold']) + x)
			session['activities'] += "<p class='green'>Earned " + str(x) + " golds from the farm! (" + y + ")</p>"
			print(session)
	return redirect('/')
if __name__=="__main__":
	app.run(debug=True)