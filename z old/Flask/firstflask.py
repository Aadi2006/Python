from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Adopt a pet</h1><br>Please yup"


@app.route('/about/')
def about():
  return "I am a young developer"




  
    
if __name__=="__main__" :
     app.run(debug=True)
