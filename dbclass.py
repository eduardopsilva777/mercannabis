from db import *

class produtos:
    
    def cadastro (self, titulo, descricao, valor, cartegoria):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""INSERT INTO produtos (titulo, descricao, valor, cartegoria)
        VALUES (?, ?, ?, ?)
        """, (titulo, descricao, valor, cartegoria))

        conn.commit()
        conn.close

    def exclusao (self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""DELETE FROM produtos WHERE id = ?
        """, (id))

        conn.commit()
        conn.close()

    def editar (self, id, titulo, descricao, valor, cartegoria):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('UPDATE produtos SET titulo = ?, descricao = ?, valor = ?, cartegoria = ?,  WHERE id = ?', (titulo, descricao, valor, cartegoria)) 
        conn.commit()
        conn.close()

    def exibir (self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM produtos")
        conn.close()
        return c.fetchall()

class users:
    None