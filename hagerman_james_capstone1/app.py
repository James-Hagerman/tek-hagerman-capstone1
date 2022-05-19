import os 
import sys
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKeyConstraint 
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from forms import AddFormProd, AddFormESP
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M@localhost/tek_tractor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

Migrate(app,db)


class Prod_price(db.Model):

    __tablename__ = 'prod_price'

    prod_code = db.Column(db.VARCHAR(20), primary_key = True)
    price = db.Column(db.Integer)
    year = db.Column(db.Integer, nullable = True, primary_key = True)
    quarter = db.Column(db.VARCHAR(4), nullable = True, primary_key = True)

    def __init__(self, prod_code, price, year, quarter):
        self.prod_code = prod_code
        self.price = price
        self.year = year
        self.quarter = quarter 


class Prod_info(db.Model):

    __tablename__ = 'prod_info'

    prod_code = db.Column(db.VARCHAR(20), ForeignKey('prod_price.prod_code'), primary_key = True)
    prod_name = db.Column(db.VARCHAR(45))
    prod_manufacturer = db.Column(db.VARCHAR(256))

    def __init__(self, prod_code, prod_name, prod_manufacture):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.prod_manufactur = prod_manufacture


class Esp_table(db.Model):

    __tablename__ = 'esp_price'

    esp_code = db.Column(db.VARCHAR(20), primary_key = True)
    price = db.Column(db.Integer, nullable = False)
    year = db.Column(db.Integer, nullable = False, primary_key = True)

    def __init__(self, esp_code, price, year):
        self.esp_code = esp_code 
        self.price = price 
        self.year = year 


class Employee(db.Model):

    __tablename__ = 'employee'

    employee_id = db.Column(db.VARCHAR(20), primary_key = True)
    employee_name = db.Column(db.VARCHAR(20), nullable = False)
    region = db.Column(db.VARCHAR(20), nullable = False)
    pay_grade = db.Column(db.VARCHAR(20), nullable = False)

    def __init__(self, employee_id, employee_name, region, pay_grade):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.region = region
        self.pay_grade = pay_grade


class Datetable(db.Model):

    __tablename__ = 'datetable'

    date = db.Column(db.VARCHAR(20), primary_key = True)
    year = db.Column(db.Integer)
    quarter = db.Column(db.VARCHAR(4))
    period = db.Column(db.Integer)
    week = db.Column(db.Integer)

    def __init__(self, date, year, quarter, period, week):
        self.date = date
        self.year = year
        self.quarter = quarter
        self.period = period
        self.week = week 

class Sales_esp(db.Model):

    __tablename__ = 'esp_sales'

    esp_sale_id = db.Column(db.Integer, primary_key = True)
    esp_code = db.Column(db.VARCHAR(20))
    emp_id = db.Column(db.VARCHAR(20), ForeignKey('employee.employee_id'))
    quantity = db.Column(db.VARCHAR(20))
    year = db.Column(db.Integer)
    date = db.Column(db.VARCHAR(20), ForeignKey('datetable.date'))
    __table_args__ = (ForeignKeyConstraint([esp_code, year], [Esp_table.esp_code, Esp_table.year]), {})

    def __init__(self, esp_code, emp_id, quantity, year, date):
        self.esp_code = esp_code
        self.emp_id = emp_id
        self.quantity = quantity
        self.year = year
        self.date = date

class Sales_prod(db.Model):

    __tablename__ = 'prod_sales'
    
    prod_sale_id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.VARCHAR(20), ForeignKey('employee.employee_id'))
    prod_code = db.Column(db.VARCHAR(20), ForeignKey('prod_info.prod_code'))
    quantity = db.Column(db.VARCHAR(20))
    year = db.Column(db.Integer)
    quarter = db.Column(db.VARCHAR(4))
    date = db.Column(db.VARCHAR(20), ForeignKey('datetable.date'))
    __table_args__ = (ForeignKeyConstraint([prod_code, year, quarter], [Prod_price.prod_code, Prod_price.year, Prod_price.quarter]), {})

    def __init__(self, emp_id, prod_code, quantity, year, quarter, date):
        self.emp_id = emp_id 
        self.prod_code = prod_code 
        self.quantity = quantity 
        self.year = year
        self.quarter = quarter
        self.date = date




db.create_all()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/prod_sales', methods = ['GET', 'POST'])
def sales_prod():

    form = AddFormProd()

    if form.validate_on_submit():
        emp_id = form.employee.data
        prod_code = form.product.data
        quantity = form.quantity.data
        year = form.year.data
        quarter = form.quarter.data 
        date = form.date.data

        new_entry = Sales_prod(emp_id, prod_code, quantity, year, quarter, date)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('prod_sales.html', form = form)

@app.route('/esp_sales', methods = ['GET', 'POST'])
def sales_esp():

    form = AddFormESP()
    
    if form.validate_on_submit():
        emp_id = form.employee.data
        esp_code = form.esp_code.data
        quantity = form.quantity.data
        year = form.year.data
        date = form.date.data

        new_entry = Sales_esp(emp_id, esp_code, quantity, year, date)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('esp_sales.html', form = form)



if __name__ == '__main__':
    app.run(debug=True)


