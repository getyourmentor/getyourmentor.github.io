from flask import Flask, render_template, flash, request, redirect, url_for, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sendgrid
from forms import *

DEBUG = True
app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app = Flask(__name__)

users = 0
mentee_count = 0

def send_mail(subject_given, users, name, email, ph_num, field, expect):
	sg = sendgrid.SendGridAPIClient(apikey = "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")#os.environ.get("SG_API_KEY"))
	from_email = sendgrid.helpers.mail.Email("rahulkumaran313@gmail.com", name="Rahul Arulkumaran")
	if(subject_given.split("-")[0]=='mentorship'):
		to_email = sendgrid.helpers.mail.Email("getyourmentor@gmail.com")
	else:
		to_email = sendgrid.helpers.mail.Email("getyourmentor_mentor@gmail.com")
	subject = subject_given
	content = sendgrid.helpers.mail.Content("text/html", "Request: %s <br>Name : %s <br>Email : %s <br>Number : %s <br>Field Of Mentorship : %s <br>Expectation of student : %s<br>"%(users, name, email, ph_num, field, expect))
	mail = sendgrid.helpers.mail.Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	return response


@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route("/mentor", methods=['GET', 'POST'])
def mentor():
	form = MentorForm(request.form)
	if(request.method == 'POST'):
		if(form.validate()):
			global users
			users+=1
			subject = "Mentorship - " + str(users)
			#response = send_mail(subject, users, request.form['name'], request.form['email'], request.form['ph_num'], request.form['mentor_field'], request.form['expect'])
			return redirect(url_for("thanks"))
	return render_template("mentor.html", form=form)

@app.route("/mentee", methods=['GET', 'POST'])
def mentee():
	form = MenteeForm(request.form)
	if(request.method == 'POST'):
		if(form.validate()):
			global mentee_count
			mentee_count += 1
			subject = "Mentee Form - " + str(mentee_count)
			#response = send_mail(subject, users, request.form['name'], request.form['email'], request.form['ph_num'], request.form['mentee'], request.form['expect'])
			return redirect(url_for("thanks"))
	return render_template("mentee.html", form=form)

@app.route("/thanks", methods=['GET', 'POST'])
def thanks():
	return render_template('thanks.html')


@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == "__main__":
	app.run()
