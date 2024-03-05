import os
import csv
import pandas as pd
import psycopg2

# Probar version de pandas: print(pd.version)
#Datos del ususario al que me voy a conectar
dbname = "Syslog"
user = "postgres"
password = "1234"
host = "10.209.202.208"
port = "5432"


#Establecer la conexion:
try:
 conn = psycopg2.connect(
  dbname=dbname,
  user=user,
  password=password,
  host=host,
  port=port, 
 )
 
 print ("Conexion exitosa")

 #Proceso de querys(consultas):
 #cur se utiliza para generar comandos sql
 cur = conn.cursor()

 #Ejecutar la consulta sql para filtrar los datos:
 #query = "SELECT id, receivedat, message FROM systemevents WHERE message LIKE '%TCP CONNECTION%';" #WHERE message LIKE '%TCP connection%'  
 #query = "SELECT id, receivedat, message FROM systemevents WHERE message LIKE %s;"
 query = "SELECT id, receivedat, message FROM systemevents WHERE message LIKE %s;"
 pattern = '%TCP connection%'  # Patrón para buscar en el mensaje

 cur.execute(query, (pattern,))#('idUsuario', 'fechaC', 'message'))

#  #Obtener los resultados
 rows = cur.fetchall()

 # Escribir los resultados en un archivo CSV
 with open('resultados_filtrados.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
        
    # Escribir el encabezado del archivo CSV
    csv_writer.writerow(['ID', 'Fecha', 'Connection','Mensaje'])

    for row in rows:
      ID = row [0]
      Fecha = row [0]
      message = row [2]

      data = message.split ()
      Connection = ' '.join(data[:3])
      Mensaje = ' '.join(data[4:])
        
    # Escribir los datos filtrados en el archivo CSV
      csv_writer.writerow([ID, Fecha, Connection, Mensaje])
      
 

 #Cerrar conexiòn
 cur.close()
 conn.close()

 print("Datos filtrados guardados en resultados_filtrados.csv")

except psycopg2.Error as e:
 print("Error al conectar a la base de datos", e)