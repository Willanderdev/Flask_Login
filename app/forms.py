# from flask_wtf import FlaskForm

# class UpdateUserForm(FlaskForm):

#     email = StringField('Email', validators=[InputRequired(
#         message='Enter a valid email'), Email()])
#     firstname = StringField('First Name', validators=[
#                             InputRequired(message='Enter your first name')])
#     lastname = StringField('Last Name', validators=[
#                            InputRequired(message='Enter your last name')])
#     submit = SubmitField('Update')

#     def validate_email(self, email):
#         if User.query.filter_by(email=email.data).first():
#             raise ValidationError('This email has been registered already!')
