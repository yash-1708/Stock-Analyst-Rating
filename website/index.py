from flask import Flask,render_template,request,flash
from recordEnterFrom import RecordEnterForm
import sqlalchemy
from datetime import datetime
import mysql.connector
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from sqlalchemy.sql import text


app=Flask(__name__)
app.config['SECRET_KEY']='b4c3f4b70ec9b4e0' #protect against key and attacks
@app.route('/',methods=['GET', 'POST'])
@app.route('/home')
def home():
    return render_template('/home/home.html')

@app.route('/recomm')
def enterRecommendation():
    form=RecordEnterForm(request.form)
    if request.method == 'POST':
        broker_name=request.form['broker_name']
        company_name=request.form['company_name']
        current_price=request.form['current_price']
        recomended_price=request.form['recomended_price']
        predict_date=request.form['predict_date']
        target_price=request.form['target_price']
        close_price=request.form['close_price']
        print(broker_name, " ", company_name, " ", current_price, " ", recomended_price, " ", predict_date, " ", target_price, " ", close_price)
        
        
        
        database_username = 'root'
        database_password = 'yash'
        database_ip       = '127.0.0.1'
        database_name     = 'mainschema'
        database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(database_username, database_password, database_ip, database_name))

        if form.validate():
        # Save the comment here.
            flash('Record added Successfully')
            result = database_connection.execute(text("INSERT INTO test(broker, company_name, current_price, recomended_buying, predict_date, target_price, close_price) VALUES ('"+broker_name+"','"+company_name+"','"+current_price+"','"+recomended_price+"','"+predict_date+"','"+target_price+"','"+close_price+"');"))

        else:
            flash('Error: occurred ')
    return render_template('/Enter_Record/recordEnter.html',form=form)


if __name__=='__main__':
    app.run(debug=True)