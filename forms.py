from wtforms import Form
from wtforms import StringField, EmailField, IntegerField, RadioField, SelectMultipleField, widgets
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Correo no válido")
    ])

class CinepolisForm(Form):
    Nombre = StringField('Nombre', [
        validators.DataRequired(message="* El nombre es obligatorio")
    ])
    CantidadCompradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message="* El campo cantidad de compradores es requerido"),
        validators.NumberRange(message="Mínimo 1 comprador")
    ])
    TarjetaCineco = RadioField(
        'Tarjeta Cineco',
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no',
        validators=[validators.DataRequired(message="Seleccione una opción")]
    )
    CantidadBoletas = IntegerField('Cantidad De Boletas', [
        validators.DataRequired(message="* El campo cantidad de boletas es requerido"),
        validators.NumberRange(min=1, max=70, message="Mínimo 1 boleta")
    ])

class ExamenParcialPizzasForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    direccion = StringField("Dirección", [
        validators.DataRequired(message="El campo es requerido")
    ])
    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El campo es requerido")
    ])
    num_pizzas = IntegerField("Número de Pizzas", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Mínimo 1 pizza")
    ])
    tamanio = RadioField(
        "Tamaño de Pizza",
        choices=[
            ('chica', 'Chica $40'), 
            ('mediana', 'Mediana $80'), 
            ('grande', 'Grande $120'), 
            ('pequeña', 'Pequeña $160')
        ],
        default='chica',
        validators=[validators.DataRequired(message="Seleccione una opción")]
    )
    ingredientes = SelectMultipleField(
        "Ingredientes",
        choices=[
            ('jamon', 'Jamón $10'), 
            ('piña', 'Piña $10'), 
            ('champiñones', 'Champiñones $10')
        ],
        default=['jamon'],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )