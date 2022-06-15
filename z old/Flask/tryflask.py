from flask import Flask

app = Flask(__name__)
myage = 14
@app.route('/')
def home():
    return '''<h1>Hey, welcome</h1>
    <p> This is a trial website, and this is the first page<br>
    <a href='/about'>My about page</a>'''

@app.route('/about')
def about():
    return '''<h2>I am Aadi what about you?</h2>
    <a href='/'>My home page</a>'''

@app.route('/intro/<name>/<int:age>')
def intro(name,age):
    return f'''<h1>Hey {name.capitalize()}!</h1>
     <h2>You're {age} years old</h2> 
     <p>I am {myage-age} years older than you '''

if __name__=="__main__" :
     app.run(debug=True)