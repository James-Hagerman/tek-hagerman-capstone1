from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField

# class AddFormAgg(FlaskForm):
    
#     name = StringField('Employee ID: ')
#     date = DateField('Todays Date (Y-M-D): ') 
#     prod_001 = IntegerField('Product 1 Quantity: ') 
#     prod_002 = IntegerField('Product 2 Quantity: ')
#     prod_003 = IntegerField('Product 3 Quantity: ')
#     prod_004 = IntegerField('Product 4 Quantity: ')
#     prod_005 = IntegerField('Product 5 Quantity: ')
#     prod_006 = IntegerField('Product 6 Quantity: ')
#     prod_007 = IntegerField('Product 7 Quantity: ')
#     prod_008 = IntegerField('Product 8 Quantity: ')
#     esp_001 = IntegerField('Extended Service Plan 1: ')
#     esp_002 = IntegerField('Extended Service Plan 2: ')
#     esp_003 = IntegerField('Extended Service Plan 3: ')
#     esp_004 = IntegerField('Extended Service Plan 4: ')
#     esp_005 = IntegerField('Extended Service Plan 5: ')
#     esp_006 = IntegerField('Extended Service Plan 6: ')
#     esp_007 = IntegerField('Extended Service Plan 7: ')
#     esp_008 = IntegerField('Extended Service Plan 8: ')
#     submit = SubmitField('Add Sales')

class AddFormProd(FlaskForm):

    employee = SelectField('Employee ID: ', choices = [('EMP224', 'EMP224'), ('EMP256', 'EMP256'), ('EMP234', 'EMP234'), ('EMP267', 'EMP267'), ('EMP290', 'EMP290')])
    date = StringField('Date of this Sunday (M/D/YYYY): ')
    product = SelectField('Product Code: ', choices =[('PROD_001', 'PROD_001'), ('PROD_002', 'PROD_002'), ('PROD_003', 'PROD_003'), ('PROD_004', 'PROD_004'), ('PROD_005', 'PROD_005'), ('PROD_006', 'PROD_006'), ('PROD_007', 'PROD_007'), ('PROD_008', 'PROD_008')])
    quantity = IntegerField('Quantity Sold: ')
    year = IntegerField('Year (YYYY): ')
    quarter = StringField('Quarter (Integer): ')
    submit = SubmitField('Add Sale')

class AddFormESP(FlaskForm):

    employee = SelectField('Employee ID: ', choices = [('EMP224', 'EMP224'), ('EMP256', 'EMP256'), ('EMP234', 'EMP234'), ('EMP267', 'EMP267'), ('EMP290', 'EMP290')])
    date = StringField('Date of this Sunday (M/D/YYYY): ')
    esp_code = SelectField('Extended Service Plan: ', choices =[('ESP_001', 'ESP_001'), ('ESP_002', 'ESP_002'), ('ESP_003', 'ESP_003'), ('ESP_004', 'ESP_004'), ('ESP_005', 'ESP_005'), ('ESP_006', 'ESP_006'), ('ESP_007', 'ESP_007'), ('ESP_008', 'ESP_008')])
    quantity = IntegerField('Quantity Sold: ')
    year = IntegerField('Year (YYYY)')
    submit = SubmitField('Add Sale')