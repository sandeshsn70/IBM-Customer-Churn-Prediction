from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class ChurnForm(FlaskForm):
    tenure = FloatField('Tenure', validators=[DataRequired()])
    monthly_charges = FloatField('Monthly Charges', validators=[DataRequired()])
    total_charges = FloatField('Total Charges', validators=[DataRequired()])

    submit = SubmitField('Predict')