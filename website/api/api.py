from flask import  Flask,jsonify,request
import mysql.connector

app=Flask(__name__)

# cnx = mysql.connector.connect(user="smarsproddbuser@mbt-smars-mysql", password='modern@1234', host="mbt-smars-mysql.mysql.database.azure.com", port=3306, database='mainschema', ssl_disabled=True)
cnx = mysql.connector.connect(user="root", password='yash', host="127.0.0.1", port=3306, database='mainschema', ssl_disabled=True)

@app.route('/getbrokerinfo/<string:year>',methods=['GET'])
def sendBrokerInfoApi():
    mycursor = cnx.cursor()
    if year == '2016' :
        sqlquery = "SELECT * FROM finalrating2016"
        elif year == '2017' :
            sqlquery = "SELECT * FROM finalrating2017"
        elif year == '2018' :
            sqlquery = "SELECT * FROM finalrating2018"
        else :
            sqlquery = "SELECT * FROM finalrating"
    
    mycursor.execute(sqlquery)
    data = mycursor.fetchall()
    print(type(data))
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)