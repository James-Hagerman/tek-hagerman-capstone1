import mysql.connector
import pandas as pd 
import csv 
import sys
from sqlalchemy import create_engine



db = mysql.connector.connect(    
    host = "localhost",
    user = "root",
    passwd = '1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M',
    database = 'tek_tractor')

# Connecting to tek_tractor database
engine = create_engine('mysql+pymysql://root:1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M@localhost/tek_tractor')
db_cursor = db.cursor()
db_cursor.execute('SET GLOBAL FOREIGN_KEY_CHECKS=0;')

# Batch loading the datetable 
csv_datetable = pd.read_csv('hagerman_james_capstone1\data\datetable.csv')
csv_datetable.to_sql('datetable', con = engine, if_exists = 'append', index = False)

# Batch loading the product price table 
csv_prod_price = pd.read_csv('hagerman_james_capstone1\data\prod_price.csv')
csv_prod_price.to_sql('prod_price', con = engine, if_exists = 'append', index = False)

# Batch loading the product information table 
csv_prod_info = pd.read_csv('hagerman_james_capstone1\data\prod_info.csv')
csv_prod_info.to_sql('prod_info', con = engine, if_exists = 'append', index = False)

# Batch loading the Extended Service Plan price table 
csv_esp_table = pd.read_csv('hagerman_james_capstone1\data\esp_price.csv')
csv_esp_table.to_sql('esp_price', con = engine, if_exists = 'append', index = False)

# Batch loading the employee table 
csv_employee = pd.read_csv('hagerman_james_capstone1\data\employee.csv')
csv_employee.to_sql('employee', con = engine, if_exists = 'append', index = False)

# Batch loading the Extended Service Plan sales table 
csv_sales_esp = pd.read_csv('hagerman_james_capstone1\data\esp_sales.csv')
csv_sales_esp.to_sql('esp_sales', con = engine, if_exists = 'append', index = False)

# Batch loading the product sales table 
csv_sales_prod = pd.read_csv('hagerman_james_capstone1\data\prod_sales.csv')
csv_sales_prod.to_sql('prod_sales', con = engine, if_exists = 'append', index = False)
