from flask import Flask
app=Flask(__name__)
@app.route('/')
# @app.route('/index')
def index():
    user = {'username': 'sumit'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''