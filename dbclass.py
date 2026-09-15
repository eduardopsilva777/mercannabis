from db import *
from flask import request, jsonify

class produtos:
<<<<<<< HEAD
=======

    def __init__(self):
        dados = request.get_json()
        titulo = dados["titulo"]
        descricao = 
    
>>>>>>> 97405987d9d18e5059e65473d0228904d82cc7da
    def cadastro (self, titulo, descricao, valor, cartegoria):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(""" INSERT INTO produtos (titulo, descricao, valor, cartegoria)
        VALUES (?, ?, ?, ?)
        """, (titulo, descricao, valor, cartegoria))

        conn.commit()
        conn.close

    def exclusao (self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(""" DELETE FROM produtos WHERE id = ?
        """, (id))

        conn.commit()
        conn.close()

    def editar (self, id, titulo, descricão, valor, cartegoria):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

    def exibir (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

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
            