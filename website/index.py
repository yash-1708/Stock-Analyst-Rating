from flask import Flask,render_template,request,flash
from recordEnterFrom import RecordEnterForm
import mysql.connector


#cnx = mysql.connector.connect(user="smarsproddbuser@mbt-smars-mysql", password='modern@1234', host="mbt-smars-mysql.mysql.database.azure.com", port=3306, database='mainschema', ssl_disabled=True)
cnx = mysql.connector.connect(user="root", password='yash', host="127.0.0.1", port=3306, database='mainschema')
app=Flask(__name__)
app.config['SECRET_KEY']='b4c3f4b70ec9b4e0' #protect against key and attacks

@app.route('/',methods=['GET', 'POST'])
@app.route('/home')
def home():
    #get records from database with rating ,Each Record must contain ID of Database
    #and store it in List
    #we will iterate this list in homepage
    mycursor = cnx.cursor()
    mycursor.execute('SELECT * FROM finalrating')
    data = mycursor.fetchall()
    title = "Broker Ratings"
    return render_template('/home/home.html', output_data = data, yearNo = title)
    #return render_template('/home/home.html', yearNo = title)



#Broker Info Page function
@app.route('/brokerInfo/<int:id>')
def brokerInfo(id):
    #fetch Broker Information On basis of id from database and store it in object
    #this object is referred from html
    return render_template('/brokerInfo/brokerInfo.html')



#Year wise Broker recommendation info function
@app.route('/yearwiseInfo')
def yearwiseInfo():
    #fetch Broker stock info yearwise Information On basis of id from database and store it in object
    #this object is referred from html
    if request.method == 'GET':
        year = request.args.get('year')
        orderBy = request.args.get('orderBy')
        mycursor = cnx.cursor()
        
        if orderBy == 'descending' :
            sqladd = " ORDER BY Rating DESC;"
        else :
            sqladd = " ORDER BY Rating ASC;"

        sqlquery = "SELECT * FROM finalrating"
        
        if year == '2016' :
            sqlquery = "SELECT * FROM finalrating2016"
        elif year == '2017' :
            sqlquery = "SELECT * FROM finalrating2017"
        elif year == '2018' :
            sqlquery = "SELECT * FROM finalrating2018"
        else :
            sqlquery = "SELECT * FROM finalrating"

        sqlquery = sqlquery + sqladd
        mycursor.execute(sqlquery)
        data = mycursor.fetchall()
        title = "Broker Ratings"
        if not year == '9999':
            title = year + " Broker Ratings"
    return render_template('/home/home.html', output_data = data, yearNo = title)

@app.route('/recommandlist')
def recommandlist():
    #this object is referred from html
    return render_template('/recommandlist/recommandlist.html')

#Add new Recommendation function
@app.route('/recomm',methods=['GET', 'POST'])
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

        if form.validate():
        # Save the comment here.
            mycursor = cnx.cursor()
            flash('Record added Successfully')
            val = (broker_name,company_name,current_price,recomended_price,predict_date,target_price,close_price)
            sql1 = "INSERT INTO test(broker, company_name, current_price, recomended_buying, predict_date, target_price, close_price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql1,val)
            cnx.commit()
            #result = cnx.execute(str("INSERT INTO test(broker, company_name, current_price, recomended_buying, predict_date, target_price, close_price) VALUES ('"+broker_name+"','"+company_name+"','"+current_price+"','"+recomended_price+"','"+predict_date+"','"+target_price+"','"+close_price+"');"))
            
        else:
            flash('Error: occurred ')
    return render_template('/Enter_Record/recordEnter.html',form=form)


if __name__=='__main__':
    app.run(debug=True)