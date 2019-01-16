from flask import Flask, render_template, flash, request, redirect, url_for, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sendgrid

DEBUG = True
app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app = Flask(__name__)

class ReusableForm(Form):
	name = TextField('* Full Name:', validators=[validators.DataRequired()])
	email = TextField('* Email ID:', validators=[validators.DataRequired()])
	ph_num = TextField('* Phone Number:', validators=[validators.DataRequired()])
	mentor_field = TextField('* Which area do you want to be mentored on?', validators=[validators.DataRequired()])
	expect = TextField('What do you expect from your mentor?', validators=[validators.DataRequired()])


def send_mail(users, name, email, ph_num, field, expect):
	sg = sendgrid.SendGridAPIClient(apikey = "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" )#os.environ.get("SG_API_KEY"))
	from_email = sendgrid.helpers.mail.Email("rahulkumaran313@gmail.com", name="Rahul Arulkumaran")
	to_email = sendgrid.helpers.mail.Email("getyourmentor@gmail.com")
	subject = "Mentorship - " + users
	content = sendgrid.helpers.mail.Content("text/html", "demo"%(request.form['name'], mail_content))
	mail = sendgrid.helpers.mail.Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	return response


@app.route("/", methods=['GET', 'POST'])
def index():
	form = ReusableForm(request.form)
	if(request.method == 'POST'):
		global users
		users+=1
		if(form.validate()):
			#response = send_mail(users)
			return render_template("thanks.html")
	return render_template("index.html", form=form)

@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == "__main__":
	app.run()
