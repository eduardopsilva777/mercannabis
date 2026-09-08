from flask import Flask, render_template
import sqlite3


app = Flask(_name_)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    cartegoria TEXT NOT NULL
                    preco REAL NOT NULL,
                    product_created_at TEXT DEFAULT CURRENT_TIMESTAMP
                    );
                ''')
    conn.commit()
    conn.close()


init_db()

@app.route("/")
def index ():
    return render_template("/index")

class produtos:
    self



if _name_ == '_main_':
    app.run(debug=True)