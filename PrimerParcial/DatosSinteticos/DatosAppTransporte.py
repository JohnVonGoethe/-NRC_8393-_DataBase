import pandas as pd# es una librería de Python especializada en el manejo y análisis de estructuras de datos.
import uuid# define un sistema para crear identificadores universalmente únicos de recursos de una manera que no requiere un registro central
import random# contiene una serie de funciones relacionadas con los valores aleatorios 
from faker import Faker# es un paquete de Python que genera datos falsos para ti. Ya sea que necesite iniciar su base de datos
import datetime# módulo proporciona clases para manipular fechas y horas.
# -*- coding: utf-8 -*-
numUsuarios = 5000 # Número de usuarios a generar
numTaxistas = 5000 # Número de taxistas a generar
numCompanias = 5000 # Número de compañías a generar
numVehiculos = 5000 # Número de vehículos a generar


features = [ # Una lista de 7 características 
    "subscriber",
    "id",
    "genero",
    "nombre",
    "email",
    "nac",
    "phone",
]
df = pd.DataFrame(columns=features)# Creamos un DataFrame con las columnas, Estructura de dos dimensiones (tablas).

choice = [True, False]# Lista de booleanos para elegir si es verdadero o falso

df['subscriber'] = random.choices(# Generar una lista aleatoria de booleanos
    choice, 
    k=numUsuarios# El número a generar
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numUsuarios)]# generamos los datos id y guardarlos en el DataFrame

print(df['id'].nunique()==numUsuarios)# Imprime verdadero si el usuario es unico 

genders = ["male", "female", "na"]

df['genero'] = random.choices(# Generar una lista aleatoria de géneros
    genders, 
    weights=(60,30,10), # 60% de hombres, 30% de mujeres y 10% de no especificado
    k=numUsuarios
)# Genera aleatoriamente el género de cada usuario

faker = Faker()# Generar los datos falsos

def name_gen(gender):# Genera un nombre basado en el género
    if gender=='male':
        return faker.name_male()# Genera un nombre de hombre segun el genero
    elif gender=='female':
        return faker.name_female()# Genera un nombre de mujer segun el genero
    
    return faker.name()# Genera de nombres para cada usuario
df['nombre'] = [name_gen(i) for i in df['genero']]# guarda el nombre en la columna name

def emailGen(name, duplicateFound=False):# Genera una dirección de correo electrónico aleatoria basada en el nombre dado

    dom = "@firemail.es"# Nombre del dominio falso para usar
    
    name = name.lower().split(" ")# Separa el nombre en dos partes
    
    chars = [".", "_"]# carácter aleatorio para insertar en el nombre
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    if duplicateFound:# adicional del correo electrónico si se encontró un duplicado
        
        num = random.randint(0,100)# Número aleatorio para insertar al final
        
        new_name = new_name + str(num)# Insertado en el final
        
    return new_name + dom # Devuelve la dirección de correo electrónico unico con el dominio

emails = []# Generar la lista de mails

for name in df['nombre']:# Generar una dirección de correo electrónico para cada nombre
    
    email = emailGen(name)# Generando el correo electrónico
    
    while email in emails:# Bucle hasta que se genere un correo electrónico único
        
        email = emailGen(name, duplicateFound=True)# Crear un correo electrónico con un número aleatorio
    
    emails.append(email)# Adjuntar el nuevo correo electrónico a la lista
    
df['email'] = emails# Guarda el mail en la columna mail

def random_nac(start, end, n):# Generar una lista aleatoria entre dos marcas de tiempo dadas
    
    frmt = "%Y-%m-%d" # El formato de tiempo
    
    stime = datetime.datetime.strptime(start, frmt)# Formatear los dos periodos de tiempo
    etime = datetime.datetime.strptime(end, frmt)
    
    td = etime - stime# Creando el grupo para tiempos aleatorios
    
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]# Generando una lista con los tiempos aleatorios
    
    return times# Generar una lista de fechas de nacimiento aleatorias

df['nac'] = random_nac("1970-01-01", "2006-01-01", numUsuarios)# guarda la fecha de nacimiento en la columna nac en un intervalo de 1970 a 2006

df['phone'] = [faker.phone_number() for i in range(numUsuarios)]# Genera un número de teléfono aleatorio para cada usuario

df.to_csv('dataset_usuarios.csv')# Guarda el DataFrame en un archivo csv

features = [ # Una lista de 7 características
    "subscriber",
    "id",
    "genero",
    "nombre",
    "email",
    "nac",
    "phone",
]
df = pd.DataFrame(columns=features)# Creamos un DataFrame para esta lista

choice = [True, False]# Lista de booleanos para elegir si es verdadero o falso

df['subscriber'] = random.choices(# Generar una lista aleatoria de booleanos
    choice, 
    k=numTaxistas# El número a generar
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numTaxistas)]# generamos los datos id y guardarlos en el DataFrame

print(df['id'].nunique()==numTaxistas)# Imprime verdadero si el usuario es unico 

genders = ["male", "female", "na"]# Lista de géneros

df['genero'] = random.choices(# Generar una lista aleatoria de géneros
    genders, 
    weights=(80,10,10), # 80% de hombres, 10% de mujeres y 10% de no especificado
    k=numTaxistas# El número a generar
)# Genera aleatoriamente el género de cada usuario


def name_gen(gender):# Genera un nombre basado en el género
    if gender=='male':
        return faker.name_male()# Genera un nombre de hombre segun el genero
    elif gender=='female':
        return faker.name_female()# Genera un nombre de mujer segun el genero
    
    return faker.name()# Genera de nombres para cada usuario
df['nombre'] = [name_gen(i) for i in df['genero']]# guarda el nombre en la columna name

def emailGen(name, duplicateFound=False):# Genera una dirección de correo electrónico aleatoria basada en el nombre dado

    dom = "@icemail.es"# Nombre del dominio falso para usar
    
    name = name.lower().split(" ")# Separa el nombre en dos partes
    
    chars = [".", "_"]# carácter aleatorio para insertar en el nombre
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    if duplicateFound:# adicional del correo electrónico si se encontró un duplicado
        
        num = random.randint(0,100)# Número aleatorio para insertar al final
        
        new_name = new_name + str(num)# Insertado en el final
        
    return new_name + dom # Devuelve la dirección de correo electrónico unico con el dominio

emails = []# Generar la lista de mails

for name in df['nombre']:# Generar una dirección de correo electrónico para cada nombre
    
    email = emailGen(name)# Generando el correo electrónico
    
    while email in emails:# Bucle hasta que se genere un correo electrónico único
        
        email = emailGen(name, duplicateFound=True)# Crear un correo electrónico con un número aleatorio
    
    emails.append(email)# Adjuntar el nuevo correo electrónico a la lista
    
df['email'] = emails# Guarda el mail en la columna mail

def random_nac(start, end, n):# Generar una lista aleatoria entre dos marcas de tiempo dadas
    
    frmt = "%Y-%m-%d" # El formato de tiempo
    
    stime = datetime.datetime.strptime(start, frmt)# Formatear los dos periodos de tiempo
    etime = datetime.datetime.strptime(end, frmt)
    
    td = etime - stime# Creando el grupo para tiempos aleatorios
    
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]# Generando una lista con los tiempos aleatorios
    
    return times# Generar una lista de fechas de nacimiento aleatorias

df['nac'] = random_nac("1970-01-01", "2002-01-01", numUsuarios)# guarda la fecha de nacimiento en la columna nac en un intervalo de 1970 a 2002

df['phone'] = [faker.phone_number() for i in range(numUsuarios)]# Genera un número de teléfono aleatorio para cada usuario

df.to_csv('dataset_taxistas.csv')# Guarda el DataFrame en un archivo csv

faker = Faker(['es_MX'])# Genera datos aleatorios en español

features = [ # Una lista de 6 características
    "subscriber",
    "id",
    "compania",
    "direccion",
    "email",
    "phone",
]
df = pd.DataFrame(columns=features)# Creamos un DataFrame para esta lista

choice = [True, False]# Lista de booleanos para elegir si es verdadero o falso

df['subscriber'] = random.choices(# Generar una lista aleatoria de booleanos
    choice, 
    k=numCompanias# El número a generar
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numCompanias)]# generamos los datos id de la compania y guardarlos en el DataFrame

df['compania'] = [faker.company() for i in range(numCompanias)]# Genera una compañía aleatoria y la guarda en el DataFrame

df['direccion'] = [faker.address() for i in range(numCompanias)]# Genera una dirección aleatoria y la guarda en el DataFrame

df['email'] = [faker.company_email() for i in range(numCompanias)]# Genera un correo electrónico de la compañía y lo guarda en el DataFrame

df['phone'] = [faker.phone_number() for i in range(numCompanias)]# Genera un número de teléfono de la compañía y lo guarda en el DataFrame

df.to_csv('dataset_companias.csv')# Guarda el DataFrame en un archivo csv

faker = Faker(['es_CO'])# Generar los datos falsos

features = [ # Una lista de 5 para vehiculos
    "subscriber",
    "id",
    "marca",
    "color",
    "placa",
]
df = pd.DataFrame(columns=features)# Creamos un DataFrame para esta lista

choice = [True, False]# Lista de booleanos para elegir si es verdadero o falso

df['subscriber'] = random.choices(# Generar una lista aleatoria de booleanos
    choice, 
    k=numVehiculos# El número a generar
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numVehiculos)]# generamos los datos id de la compania y guardarlos en el DataFrame

marcas =["audi", "bmw", "ford", "mercedes", "toyota", "volkswagen", "volvo", "seat", "renault", "citroen", "peugeot", "hyundai", "kia", "nissan"]
# Lista de marcas de coches
df['marca'] = random.choices(# Generar una lista aleatoria de marcas de coches
    marcas, 
    k=numVehiculos# El número a generar
)# Genera aleatoriamente marca de cada usuario

df['color'] = [faker.color_name() for i in range(numVehiculos)]# Genera un color aleatorio y lo guarda en el DataFrame

df['placa'] = [faker.license_plate() for i in range(numVehiculos)]# Genera una matricula aleatoria y la guarda en el DataFrame

df.to_csv('dataset_vehiculos.csv')# Guarda el DataFrame en un archivo csv





    


