from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,DateField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo

class RecordEnterForm(FlaskForm):
    broker_name=StringField('Broker Name',validators=[DataRequired(),Length(min=1)])
    company_name=StringField('Company Name',validators=[DataRequired(),Length(min=1)])
    current_price=FloatField('Current Price',validators=[DataRequired()])
    recomended_price=FloatField('Recomended Price',validators=[DataRequired()])
    predict_date=DateField('Predict Date',validators=[DataRequired()])
    target_price=FloatField('Target Price',validators=[DataRequired()])
    close_price=FloatField('Close Price',validators=[DataRequired()])
    submit=SubmitField('Submit')