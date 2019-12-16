from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired


class BuildIdForm(FlaskForm):
    firmware_build_id = StringField('Firmware Buid Id',validators=[DataRequired()])
    submit = SubmitField('Confirm')




