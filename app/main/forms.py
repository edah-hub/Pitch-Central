from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import InputRequired,Email
from ..models import User

# class Comment(FlaskForm):

#     title = StringField('Comment Title',validators=[InputRequired()])
#     review = TextAreaField('pitch comment')
#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
