from db import *

class produtos:
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
    None