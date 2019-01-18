from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class MentorForm(Form):
	name = TextField('Full Name *', validators=[validators.DataRequired()])
	email = TextField('Email ID *', validators=[validators.DataRequired()])
	ph_num = TextField('Phone Number *', validators=[validators.DataRequired()])
	mentor_field = TextField('Which area do you want to be mentored on? *', validators=[validators.DataRequired()])
	expect = TextField('What do you expect from your mentor? *', validators=[validators.DataRequired()])

class MenteeForm(Form):
	name = TextField('Full Name *', validators=[validators.DataRequired()])
	email = TextField('Email ID *', validators=[validators.DataRequired()])
	ph_num = TextField('Phone Number *', validators=[validators.DataRequired()])
	mentee = TextField('Which areas can you help people with? *', validators=[validators.DataRequired()])
	expect = TextField('What do you expect in return? *', validators=[validators.DataRequired()])
