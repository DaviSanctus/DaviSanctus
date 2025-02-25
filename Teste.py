import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

#consultar dados
cursor.execute("select * from agenda")
resultado = cursor.fetchall()
for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")

cursor.close()
conexao.close()
