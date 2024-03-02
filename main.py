from flask import Flask
app = Flask(__name__)
@app.route('/home')

def HelloWorld():
    return"Hello world, I am doing tests with the fremwork flask"
#para hacer el debugg hay que agregar el siguiente parametro 
app.run(host='127.0.0.1', port = 81, debug=True)