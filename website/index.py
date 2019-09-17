from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sumit'}
    return render_template('/Enter_Record/recordEnter.html')

if __name__=='__main__':
    app.run(debug=True)