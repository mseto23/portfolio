import os
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/')
def my_home():
	return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static\\images'), 
			'favicon.ico', mimetype='image/vnd.microsoft.icon')

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		print(app.root_path)
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'Email: {email} \nSubject: {subject} \nMessage: {message} \n\n')

def write_to_csv(data):
	with open('database.csv', mode='a') as database_csv:
		print(app.root_path)
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database_csv, delimiter=',', quotechar='|', lineterminator='\n', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'Error. Please try again. '