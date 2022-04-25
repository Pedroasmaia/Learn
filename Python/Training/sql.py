from ctypes import py_object
from itertools import count
from optparse import Values
from colorama import Cursor
from numpy import insert
import pyodbc
import os

driver='{ODBC Driver 17 for SQL Server};'
server='sql-adf-teste.database.windows.net'
database='sqldb-adf-two'
username=''
password=''

conexao = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
print('200')


cursor = conexao.cursor()

read = """select max(id_computer) from dbo.computer"""

m = cursor.execute(read)

print(m)

#id_pc = m+1
#marca = input('Qual a marca do computador?')
#country = input('Qual estado você mora?')
#ram = int(input('Quanto de ram tem sua máquina?'))



#comando = f"""INSERT INTO dbo.computer(id_computer,marca,country,memory) Values({id_pc},'{marca}','{country}',{ram})"""

#cursor.execute(comando)
#cursor.commit()#Se precisa editar alguma informação
