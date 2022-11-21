import pandas as pd
import uuid
import random
from faker import Faker
import datetime

numUsuarios = 5000
numTaxistas = 5000
numCompanias = 5000
numVehiculos = 5000


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

df['subscriber'] = random.choices(
    choice, 
    k=numUsuarios
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numUsuarios)]# generamos los datos id y guardarlos en el DataFrame

print(df['id'].nunique()==numUsuarios)# Imprime verdadero si el usuario es unico 

genders = ["male", "female", "na"]

df['genero'] = random.choices(
    genders, 
    weights=(60,30,10), # 60% de hombres, 30% de mujeres y 10% de no especificado
    k=numUsuarios
)# Genera aleatoriamente el género de cada usuario

faker = Faker()

def name_gen(gender):# Genera un nombre basado en el género
    if gender=='male':
        return faker.name_male()
    elif gender=='female':
        return faker.name_female()
    
    return faker.name()# Genera de nombres para cada usuario
df['nombre'] = [name_gen(i) for i in df['genero']]# guarda el nombre en la columna name

def emailGen(name, duplicateFound=False):# Genera una dirección de correo electrónico aleatoria basada en el nombre dado

    dom = "@firemail.es"# Nombre del dominio falso para usar
    
    name = name.lower().split(" ")
    
    chars = [".", "_"]# carácter aleatorio para insertar en el nombre
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    if duplicateFound:# adicional del correo electrónico si se encontró un duplicado
        
        num = random.randint(0,100)# Número aleatorio para insertar al final
        
        new_name = new_name + str(num)# Insertado en el final
        
    return new_name + dom # Devuelve la dirección de correo electrónico unico con el dominio

emails = []

for name in df['nombre']:
    
    # Generating the email
    email = emailGen(name)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(name, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
df['email'] = emails

def random_nac(start, end, n):# Generar una lista aleatoria entre dos marcas de tiempo dadas
    
    frmt = "%Y-%m-%d" # El formato de tiempo
    
    stime = datetime.datetime.strptime(start, frmt)# Formatear los dos periodos de tiempo
    etime = datetime.datetime.strptime(end, frmt)
    
    td = etime - stime# Creando el grupo para tiempos aleatorios
    
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]# Generando una lista con los tiempos aleatorios
    
    return times

df['nac'] = random_nac("1970-01-01", "2006-01-01", numUsuarios)# guarda la fecha de nacimiento en la columna nac

df['phone'] = [faker.phone_number() for i in range(numUsuarios)]# Genera un número de teléfono aleatorio para cada usuario

df.to_csv('dataset_usuarios.csv')

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

df['subscriber'] = random.choices(
    choice, 
    k=numTaxistas
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numTaxistas)]# generamos los datos id y guardarlos en el DataFrame

print(df['id'].nunique()==numTaxistas)# Imprime verdadero si el usuario es unico 

genders = ["male", "female", "na"]

df['genero'] = random.choices(
    genders, 
    weights=(80,10,10), # 80% de hombres, 10% de mujeres y 10% de no especificado
    k=numTaxistas
)# Genera aleatoriamente el género de cada usuario

faker = Faker()

def name_gen(gender):# Genera un nombre basado en el género
    if gender=='male':
        return faker.name_male()
    elif gender=='female':
        return faker.name_female()
    
    return faker.name()# Genera de nombres para cada usuario
df['nombre'] = [name_gen(i) for i in df['genero']]# guarda el nombre en la columna name

def emailGen(name, duplicateFound=False):# Genera una dirección de correo electrónico aleatoria basada en el nombre dado

    dom = "@icemail.es"# Nombre del dominio falso para usar
    
    name = name.lower().split(" ")
    
    chars = [".", "_"]# carácter aleatorio para insertar en el nombre
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    if duplicateFound:# adicional del correo electrónico si se encontró un duplicado
        
        num = random.randint(0,100)# Número aleatorio para insertar al final
        
        new_name = new_name + str(num)# Insertado en el final
        
    return new_name + dom # Devuelve la dirección de correo electrónico unico con el dominio

emails = []

for name in df['nombre']:
    
    # Generating the email
    email = emailGen(name)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(name, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
df['email'] = emails

def random_nac(start, end, n):# Generar una lista aleatoria entre dos marcas de tiempo dadas
    
    frmt = "%Y-%m-%d" # El formato de tiempo
    
    stime = datetime.datetime.strptime(start, frmt)# Formatear los dos periodos de tiempo
    etime = datetime.datetime.strptime(end, frmt)
    
    td = etime - stime# Creando el grupo para tiempos aleatorios
    
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]# Generando una lista con los tiempos aleatorios
    
    return times

df['nac'] = random_nac("1970-01-01", "2002-01-01", numUsuarios)# guarda la fecha de nacimiento en la columna nac

df['phone'] = [faker.phone_number() for i in range(numUsuarios)]# Genera un número de teléfono aleatorio para cada usuario

df.to_csv('dataset_taxistas.csv')

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

df['subscriber'] = random.choices(
    choice, 
    k=numCompanias
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numCompanias)]# generamos los datos id de la compania y guardarlos en el DataFrame

df['compania'] = [faker.company() for i in range(numCompanias)]# Genera una compañía aleatoria y la guarda en el DataFrame

df['direccion'] = [faker.address() for i in range(numCompanias)]# Genera una dirección aleatoria y la guarda en el DataFrame

df['email'] = [faker.company_email() for i in range(numCompanias)]# Genera un correo electrónico de la compañía y lo guarda en el DataFrame

df['phone'] = [faker.phone_number() for i in range(numCompanias)]# Genera un número de teléfono de la compañía y lo guarda en el DataFrame

df.to_csv('dataset_companias.csv')

features = [ # Una lista de 5
    "subscriber",
    "id",
    "marca",
    "color",
    "matricula",
]
df = pd.DataFrame(columns=features)# Creamos un DataFrame para esta lista

choice = [True, False]# Lista de booleanos para elegir si es verdadero o falso

df['subscriber'] = random.choices(
    choice, 
    k=numVehiculos
)# Guarda aleatoriamente la suscripción con verdadero o falso

df['id'] = [uuid.uuid4().hex for i in range(numVehiculos)]# generamos los datos id de la compania y guardarlos en el DataFrame

marcas =["audi", "bmw", "ford", "mercedes", "toyota", "volkswagen", "volvo", "seat", "renault", "citroen", "peugeot", "hyundai", "kia", "nissan"]

df['marca'] = random.choices(
    marcas, 
    k=numVehiculos
)# Genera aleatoriamente marca de cada usuario

df['color'] = [faker.color_name() for i in range(numVehiculos)]# Genera un color aleatorio y lo guarda en el DataFrame

df['matricula'] = [faker.license_plate() for i in range(numVehiculos)]# Genera una matricula aleatoria y la guarda en el DataFrame

df.to_csv('dataset_vehiculos.csv')