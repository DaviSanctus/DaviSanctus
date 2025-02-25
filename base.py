import sqlite3
dados = [("João", "987878615"),
         ("André", "987754118"),
         ("Maria", "987936281"),
         ("Davi", "994398587")]

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute('''
    create table agenda(nome text,
                        telefone text)
''')
cursor.executemany('''
    insert into agenda(nome, telefone)
        values(?, ?)
''', dados)

conexao.commit()
cursor.close()
conexao.close()
