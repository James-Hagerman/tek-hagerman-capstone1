from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class AddFormProd(FlaskForm):

    employee = SelectField('Employee ID: ', choices = [('EMP224', 'EMP224'), ('EMP256', 'EMP256'), ('EMP234', 'EMP234'), ('EMP267', 'EMP267'), ('EMP290', 'EMP290')])
    date = StringField('Date of this Sunday ', validators = [DataRequired()])
    product = SelectField('Product Code: ', choices =[('PROD_001', 'PROD_001'), ('PROD_002', 'PROD_002'), ('PROD_003', 'PROD_003'), ('PROD_004', 'PROD_004'), ('PROD_005', 'PROD_005'), ('PROD_006', 'PROD_006'), ('PROD_007', 'PROD_007'), ('PROD_008', 'PROD_008')])
    quantity = IntegerField('Quantity Sold ', validators = [DataRequired()])
    year = IntegerField('Year ', validators = [DataRequired()])
    quarter = StringField('Quarter ', validators = [DataRequired()])
    submit = SubmitField('Add Sale')

class AddFormESP(FlaskForm):

    employee = SelectField('Employee ID: ', choices = [('EMP224', 'EMP224'), ('EMP256', 'EMP256'), ('EMP234', 'EMP234'), ('EMP267', 'EMP267'), ('EMP290', 'EMP290')])
    date = StringField('Date of this Sunday ', validators = [DataRequired()])
    esp_code = SelectField('Extended Service Plan ', choices =[('ESP_001', 'ESP_001'), ('ESP_002', 'ESP_002'), ('ESP_003', 'ESP_003'), ('ESP_004', 'ESP_004'), ('ESP_005', 'ESP_005'), ('ESP_006', 'ESP_006'), ('ESP_007', 'ESP_007'), ('ESP_008', 'ESP_008')])
    quantity = IntegerField('Quantity Sold ', validators = [DataRequired()])
    year = IntegerField('Year ', validators = [DataRequired()])
    submit = SubmitField('Add Sale')