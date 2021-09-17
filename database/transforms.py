
import pandas as pd
import requests
import json

#    REFISTROS HABITUALES
all_books = ["/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/APP/database/data_base_artificial.csv"]
li = []

for f in all_books:
    tmp = pd.read_csv(f, delimiter=',')
    li.append(tmp)

DB = pd.concat(li, axis=0, ignore_index=True)
'''
path = 'http://127.0.0.1:5000/api/v1.0/placa/'

for i in range(len(DB)):
#for i in range(1):
    datos = {'placa': DB['PLACA'][i],
    'fecha': DB['FECHA'][i],
    'posicion': DB['POSICION'][i],
    'tipo': DB['TIPO'][i],
    'match': DB['MATCH'][i]
             }
    resp = requests.post(path, json=datos)
    if resp.status_code == 201:
      print('OK!')
    else:
      print('Error!!')
'''
    
#****************************************************************************************************************
#   CARGA LISTA NEGRA
all_books = ["/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/lista_interes.csv"]
li = []

for f in all_books:
    tmp = pd.read_csv(f, delimiter=',')
    li.append(tmp)

DT = pd.concat(li, axis=0, ignore_index=True)
'''
black_path = 'http://127.0.0.1:5000/api/v1.0/black'

for i in range(len(DT)):
#for i in range(1):
    black = {'placanegra': DT['PLACA'][i],
    'fechanegra': DT['FECHA'][i],
    'status': DT['STATUS'][i]
             }
    resp_black = requests.post(black_path, json=black)
    if resp_black.status_code == 201:
     print('OK!')
    else:
     print('Error!!')

    
# LEE LISTA NEGRA

resp = requests.get(black_path)
if resp.status_code == 200:
    print('OK!')
else:
    print('Error!!')

r = resp.text

j = json.loads(r)
df = pd.DataFrame.from_records(j)
'''
    
    
    
    


