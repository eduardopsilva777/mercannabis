from db import *
from flask import request, jsonify

class produtos:

    def __init__(self, id, titulo, descricao, valor, cartegoria):
        dados = request.get_json()
        self.titulo = dados["titulo"]
        self.descricao = dados["descricao"]
        self.valor = dados["valor"]
        self.cartegoria = ["cartegoria"]

    
    def cadastro (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""INSERT INTO produtos (titulo, descricao, valor, cartegoria)
        VALUES (?, ?, ?, ?)
        """, (self.titulo, self.descricao, self.valor, self.cartegoria))

        conn.commit()
        conn.close

    def exclusao (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""DELETE FROM produtos WHERE id = ?
        """, (self.id))

        conn.commit()
        conn.close()

    def editar (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('UPDATE produtos SET titulo = ?, descricao = ?, valor = ?, cartegoria = ?,  WHERE id = ?', (self.titulo, self.descricao, self.valor, self.cartegoria)) 
        conn.commit()
        conn.close()

    def exibir (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM produtos")
        conn.close()
        return c.fetchall()

class users:
    def login(self, username, password):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""
            SELECT id, username, password FROM users WHERE username = ?
            """,
            (username,)
            
        )
        
        usuario = c.fetchone()
        
        if usuario:
            print("LOGIN EFETUADO COM SUCESSO.")
        else:
            print("USUARIO NAO EXISTE")