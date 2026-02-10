import math
#se realiza la importación de flask
from flask import Flask, render_template,request
import forms
from flask_wtf.csrf import CSRFProtect
#se coloca el nombre
app = Flask(__name__)
app.secret_key='clave_secreta'
csrf=CSRFProtect()
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

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat, nom, ape, email = 0, "", "", ""
    alumno_clas = forms.UserForm(request.form)
    
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data 
        
    return render_template("alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)
@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    form = forms.CinepolisForm(request.form)
    valor_a_pagar = ""
    mensaje_error = ""
    
    if request.method == 'POST':
        if form.validate():
            cant_compradores = form.CantidadCompradores.data
            cant_boletas = form.CantidadBoletas.data
            tarjeta = form.TarjetaCineco.data
            
            max_permitido = cant_compradores * 7
            
            if cant_boletas > max_permitido:
                mensaje_error = f"No se pueden comprar más de 7 boletas por persona (Máx: {max_permitido})"
            else:
                precio_unidad = 12.00
                subtotal = cant_boletas * precio_unidad
                
                if cant_boletas > 5:
                    descuento = 0.15
                elif 3 <= cant_boletas <= 5:
                    descuento = 0.10
                else:
                    descuento = 0.0
                
                total = subtotal * (1 - descuento)
                
                if tarjeta == 'si':
                    total = total * 0.90
                
                valor_a_pagar = f"{total:,.0f}"
            
    return render_template('cinepolis.html', form=form, valor_a_pagar=valor_a_pagar, mensaje_error=mensaje_error)

@app.route('/Examen_Parcial_Pizzas', methods=['GET', 'POST'])
def ExamenParcialPizzas():
    form = forms.ExamenParcialPizzasForm(request.form)
    pizzas = []
    total_general = 0
    name = ""
    direccion = ""
    telefono = ""
    
    if request.method == 'POST' and form.validate():
        name = form.nombre.data
        direccion = form.direccion.data
        telefono = form.telefono.data
        num_pizzas = form.num_pizzas.data
        tamanio = form.tamanio.data
        ingredientes = form.ingredientes.data  
        
        precios_tamanio = {
            'chica': 40,
            'mediana': 80,
            'grande': 120,
            'pequeña': 160
        }
        
        precios_ingredientes = {
            'jamon': 10,
            'piña': 10,
            'champiñones': 10
        }
        
        textos_tamanio = {
            'chica': 'Chica',
            'mediana': 'Mediana',
            'grande': 'Grande',
            'pequeña': 'Pequeña'
        }
        
        textos_ingredientes = {
            'jamon': 'Jamón',
            'piña': 'Piña',
            'champiñones': 'Champiñones'
        }
        
        precio_tamanio = precios_tamanio[tamanio]
        precio_ingredientes = 0
        ingredientes_text = []
        
        if ingredientes:
            precio_ingredientes = sum(precios_ingredientes[i] for i in ingredientes)
            ingredientes_text = [textos_ingredientes[i] for i in ingredientes]
        
        total_por_pizza = precio_tamanio + precio_ingredientes
        
        for i in range(num_pizzas):
            pizza = {
                'numero': i + 1,
                'tamanio': textos_tamanio[tamanio],
                'ingredientes': ', '.join(ingredientes_text) if ingredientes_text else "Ninguno",
                'total': total_por_pizza
            }
            pizzas.append(pizza)
        
        total_general = total_por_pizza * num_pizzas
        
        return render_template('Examen_Parcial_Pizzas.html',  form=form, name=name, direccion=direccion,telefono=telefono,pizzas=pizzas,total_general=total_general)
    
    return render_template('Examen_Parcial_Pizzas.html', form=form)
if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)