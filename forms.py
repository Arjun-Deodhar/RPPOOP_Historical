from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField


class LatLongForm(FlaskForm):
    place_lat   = DecimalField('Latitude')
    place_long  = DecimalField('Longitude')
    place_name  = StringField('Name of Location')
    place_desc  = StringField('Enter Description')
    submit      = SubmitField('Submit')

