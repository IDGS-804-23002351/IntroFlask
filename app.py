import math
#se realiza la importación de flask
from flask import Flask, render_template,request
#se coloca el nombre
app = Flask(__name__)

#este es un decorador
@app.route('/')

#se agrega la primera funcion de la ruta principal
def home():
    title = "Pagina - Intro Flask"
    listado = ['Juan','Ana','Pedro','Luisa']
    return render_template('index.html',title=title, listado=listado)
@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')
@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')
#se agrega la segunda funcion de una ruta creada despues de la principal
@app.route("/hola")
def func():
    return 'Hola'
#se agrega la tercera funcion enviando datos string de una ruta creada despues de la principal
@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Número:{n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f'<h1>Hola {username} y tu id es: {id}</h1>'

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f'<h1>La suma es: {n1+n2}</h1>'

@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(param="juan"):
    return f'<h1>Hola, {param}</h1>'

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="name">apaterno:</label>
            <input type="text" id="name" name="name" required>
            <br>
             <input type="submit" value="Submit">
        </form>
    '''
@app.route("/operasBas",methods=['GET','POST'])
def operasBas():
    res = None
    tipoOperacion = ''
    n1 = 0
    n2 = 0
    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        if request.form.get('operacion')=='suma':
            res = float(n1)+float(n2)
            tipoOperacion = '+'
        elif request.form.get('operacion')=='resta':
            res = float(n1)-float(n2)
            tipoOperacion = '-'
        elif request.form.get('operacion')=='multiplicar':
            res = float(n1)*float(n2)
            tipoOperacion = '*'
        elif request.form.get('operacion')=='dividir':
            res = float(n1)/float(n2)
            tipoOperacion = '%'
    return render_template('operasBas.html',res=res,n1=n1,n2=n2,tipoOperacion=tipoOperacion)
@app.route("/resultado",methods=['GET','POST'])
def resul1():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'
@app.route("/DistanciaEntrePuntos",methods=['GET','POST'])
def DistanciaEntrePuntos():
    res = None
    n1 = 0
    n2 = 0
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        y1 = request.form.get('y1')
        y2 = request.form.get('y2')
        op1= int(x1)-int(x2)
        op2= int(y1)-int(y2)
        op3= math.pow(op1,2)
        op4= math.pow(op2,2)
        res = math.sqrt((op3)+(op4))
    return render_template('DistanciaEntrePuntos.html',res=res)
if __name__ == '__main__':
    app.run(debug=True)