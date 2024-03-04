from flask import Flask, request, make_response, redirect, render_template
#render template es para renderizar html dede python esto lo hace con la libreria
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
items = ['arroz', 'huevos', 'cafe', 'leche']   
@app.route('/index')
def index():
    # El objeto request contiene toda la información que viene del cliente.
    user_ip_information = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip_information)
    return response

@app.route('/hello')  # Creamos una nueva ruta que no estaba en el programa.
def hello():  # Nombre de función corregido para mejor claridad
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'items': items
    }                                               #el context con dos asterscos desempaqueta el diccionario 
    return render_template('ip_information.html', **context)  # Corregido para que se muestre el valor de user_ip, la prmer avariableantes del igual debe ser igual ue en el html

@app.route('/home')

def HelloWorld():
    return"Hello world, I am doing tests with the fremwork flask"

#para hacer el debugg hay que agregar el siguiente parametro 
app.run(host='127.0.0.1', port = 81, debug=True)

