from flask import Flask,render_template,request,flash
from recordEnterFrom import RecordEnterForm
app=Flask(__name__)
app.config['SECRET_KEY']='b4c3f4b70ec9b4e0' #protect against key and attacks
@app.route('/',methods=['GET', 'POST'])
@app.route('/index')
def index():
    form=RecordEnterForm(request.form)
    if request.method == 'POST':
        broker_name=request.form['broker_name']
        company_name=request.form['company_name']
        current_price=request.form['current_price']
        recommanded_price=request.form['recommanded_price']
        predict_date=request.form['predict_date']
        target_price=request.form['target_price']
        close_price=request.form['close_price']
        print(broker_name, " ", company_name, " ", current_price, " ", recommanded_price, " ", predict_date, " ", target_price, " ", close_price)
    
        if form.validate():
        # Save the comment here.
            flash('Record added Successfully')
        else:
            flash('Error: occurred ')
        flash(' ')
    return render_template('/Enter_Record/recordEnter.html',form=form)

if __name__=='__main__':
    app.run(debug=True)